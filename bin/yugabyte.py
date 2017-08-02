#!/usr/bin/env python

# Copyright (c) YugaByte, Inc.
"""Base script to run yugabyte processes locally.

Example use cases:

Creating a cluster with default settings
  yugabyte.py create

Creating a cluster with replication factor 5
  yugabyte.py --rf 5 create

Checking the status of your cluster
  yugabyte.py status

Adding a node to a running cluster
  yugabyte.py add_node

Stopping node #2 from your cluster
  yugabyte.py remove_node 2

Destroying your local cluster and its data
  yugabyte.py destroy
"""

import argparse
import errno
import logging
import signal
import shutil
import subprocess
import time
import os


class ClusterOptions():
    DAEMON_TYPES = ["master", "tserver"]

    def __init__(self):
        self.max_daemon_index = 20
        self.replication_factor = None
        self.base_local_url = "127.0.0.1"

        self.cluster_base_dir = "/tmp/yugabyte-local-cluster"

        self.custom_binary_dir = None
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.build_bin_dir = os.path.realpath(
                os.path.join(self.script_dir, "..", "build", "latest", "bin"))

        self.wal_dir_suffixes = ["wal1", "wal2"]
        self.data_dir_suffixes = ["data1", "data2"]
        self.log_dir_suffix = "logs"

        self.placement_cloud = "cloud"
        self.placement_region = "region"
        self.placement_zone = "zone"

        self.master_addresses = ""
        self.base_ports = {
                "master": {
                    "http": 7000,
                    "rpc": 7100
                },
                "tserver": {
                    "http": 9000,
                    "rpc": 9100,
                    "redis_http": 11000,
                    "redis_rpc": 10100,
                    "cql_http": 12000,
                    "cql_rpc": 9042
                }
        }

    def update_options_from_args(self, args):
        self.replication_factor = args.replication_factor
        self.custom_binary_dir = args.binary_dir

    def validate_daemon_type(self, daemon_type):
        if daemon_type not in ClusterOptions.DAEMON_TYPES:
            raise RuntimeError("Invalid daemon type: {}".format(daemon_type))
        # Validate the binary.
        self.get_binary_path(daemon_type)

    def validate_daemon_index(self, daemon_index):
        if daemon_index < 1 or daemon_index > self.max_daemon_index:
            raise RuntimeError("Invalid daemon index: {}".format(daemon_index))

    def get_binary_path(self, daemon_type):

        # If the user specified a custom path, do not default back to anything else.
        if self.custom_binary_dir:
            binary_dirs = [self.custom_binary_dir]
            logging.info("Using custom binaries path: {}".format(self.custom_binary_dir))
        else:
            binary_dirs = [self.script_dir, self.build_bin_dir]

        for binary_dir in binary_dirs:
            path = os.path.join(binary_dir, "yb-{}".format(daemon_type))
            if not os.path.isfile(path) or not os.access(path, os.X_OK):
                logging.debug("Binary path {} is not the yugabyte server".format(path))
            else:
                return path
        raise RuntimeError("Could not find binary for {}".format(daemon_type))

    def get_node_name(self, daemon_type, daemon_index):
        self.validate_daemon_type(daemon_type)
        self.validate_daemon_index(daemon_index)
        return "{}-{}".format(daemon_type, daemon_index)

    def get_base_node_dir(self, daemon_type, daemon_index):
        return "{}/{}".format(self.cluster_base_dir, self.get_node_name(daemon_type, daemon_index))

    def get_address(self, daemon_type, daemon_index, port_type, include_base_url=False):
        port_str = str(self.base_ports[daemon_type][port_type] + daemon_index)
        return port_str if not include_base_url else "{}:{}".format(self.base_local_url, port_str)


class ClusterControl():
    def __init__(self):
        self.options = ClusterOptions()
        self.args = None

        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers()
        self.setup_parsing()

    def setup_base_parser(self, command, help=None):
        p = self.subparsers.add_parser(command, help=help)
        func = getattr(self, command, None)
        if not func:
            raise RuntimeError("Invalid command: {}".format(command))
        p.set_defaults(func=func)
        return p

    def setup_parsing(self):
        self.parser.add_argument(
            "--binary_dir", default=None,
            help="Specify a custom directory in which to find the yugabyte binaries.")
        self.parser.add_argument(
            "--replication_factor", "--rf", default=3, type=int,
            help="Replication factor for the cluster as well as default number of masters. ")

        p = self.setup_base_parser("create", help="Create a new cluster")

        p = self.setup_base_parser("destroy", help="Destroy the current cluster")

        p = self.setup_base_parser("status", help="Get info on the current cluster processes")

        p = self.setup_base_parser("add_node", help="Add a new tserver to the current cluster")

        p = self.setup_base_parser("remove_node", help="Remove a tserver from the current cluster")
        p.add_argument("node_id", type=int, help="The index of the tserver to remove")

    def run(self):
        self.args = self.parser.parse_args()
        self.options.update_options_from_args(self.args)
        self.args.func()

    def set_master_addresses(self, server_counts):
        self.options.master_addresses = ",".join(
            [self.options.get_address("master", i, "rpc", True)
             for i in range(1, server_counts + 1)])

    def get_number_servers(self, daemon_type):
        top_level = self.options.cluster_base_dir
        dirs = os.listdir(top_level) \
            if os.path.exists(top_level) and os.path.isdir(top_level) \
            else []
        return len([dir for dir in dirs if dir.startswith(daemon_type)])

    def get_pid(self, daemon_type, daemon_index):
        try:
            return int(subprocess.check_output(
                ["pgrep", "-f", "yb-{} .* --rpc_bind_addresses {}".format(
                    daemon_type,
                    self.options.get_address(
                        daemon_type, daemon_index, "rpc", include_base_url=True))]))
        except subprocess.CalledProcessError as e:
            # From man pgrep
            #
            # EXIT STATUS
            # 0      One or more processes matched the criteria.
            # 1      No processes matched.
            # 2      Syntax error in the command line.
            # 3      Fatal error: out of memory etc.
            if e.returncode != 1:
                raise RuntimeError("Error during pgrep: {}".format(e.output))
            return 0

    def build_command(self, daemon_type, daemon_index, specific_arg_list):
        node_base_dir = self.options.get_base_node_dir(daemon_type, daemon_index)

        command_list = [
            # Start with the actual binary
            self.options.get_binary_path(daemon_type),
            # Add in all the shared flags
            "--fs_data_dirs \"{}\"".format(",".join(["{}/{}".format(
                  node_base_dir, d) for d in self.options.data_dir_suffixes])),
            "--fs_wal_dirs \"{}\"".format(",".join(["{}/{}".format(
                  node_base_dir, d) for d in self.options.wal_dir_suffixes])),
            "--log_dir \"{}/{}\"".format(node_base_dir, self.options.log_dir_suffix),
            "--webserver_port {}".format(
                self.options.get_address(daemon_type, daemon_index, "http")),
            "--rpc_bind_addresses {}".format(
                    self.options.get_address(daemon_type, daemon_index, "rpc", True)),
            "--placement_cloud {}".format(self.options.placement_cloud),
            "--placement_region {}".format(self.options.placement_region),
            "--placement_zone {}".format(self.options.placement_zone)
        ]
        binary_path = self.options.get_binary_path(daemon_type)
        www_path = os.path.realpath(os.path.join(os.path.dirname(binary_path), "..", "www"))
        if os.path.isdir(www_path):
            command_list.append("--webserver_doc_root \"{}\"".format(www_path))
        # Add custom args per type of server
        command_list.extend(specific_arg_list)
        # Redirect out and err and launch in the background
        command_list.append(">\"{0}/{1}.out\" 2>\"{0}/{1}.err\" &".format(
            node_base_dir, daemon_type))
        return " ".join(command_list)

    def get_master_only_flags(self, daemon_index):
        command_list = [
            "--create_cluster=true",
            "--master_addresses {}".format(self.options.master_addresses)
        ]
        return command_list

    def get_tserver_only_flags(self, daemon_index):
        daemon_type = "tserver"
        return [
            "--tserver_master_addrs {}".format(self.options.master_addresses),
            "--memory_limit_hard_bytes {}".format(256 * 1024 * 1024),
            "--redis_proxy_webserver_port {}".format(
                self.options.get_address(daemon_type, daemon_index, "redis_http")),
            "--redis_proxy_bind_address {}".format(
                self.options.get_address(daemon_type, daemon_index, "redis_rpc", True)),
            "--cql_proxy_webserver_port {}".format(
                self.options.get_address(daemon_type, daemon_index, "cql_http")),
            "--cql_proxy_bind_address {}".format(
                self.options.get_address(daemon_type, daemon_index, "cql_rpc", True)),
            "--local_ip_for_outbound_sockets {}".format(self.options.base_local_url)
        ]

    def start_daemon(self, daemon_type, daemon_index):
        self.options.validate_daemon_type(daemon_type)
        self.options.validate_daemon_index(daemon_index)
        node_name = "{}-{}".format(daemon_type, daemon_index)

        if not os.path.isdir(self.options.cluster_base_dir):
            raise RuntimeError("Found no cluster data at {}, cannot add node...".format(
                self.options.cluster_base_dir))

        suffixes = self.options.wal_dir_suffixes + self.options.data_dir_suffixes
        suffixes += [self.options.log_dir_suffix]
        for suffix in suffixes:
            path = os.path.join(self.options.cluster_base_dir, node_name, suffix)
            if not os.path.exists(path):
                os.makedirs(path)

        custom_flags = []
        if daemon_type == "master":
            custom_flags = self.get_master_only_flags(daemon_index)
        else:
            custom_flags = self.get_tserver_only_flags(daemon_index)
        command = self.build_command(daemon_type, daemon_index, custom_flags)
        logging.info("Starting {} with:\n{}".format(daemon_type, command))
        os.system(command)

    def stop_daemon(self, daemon_type, daemon_index):
        pid = self.get_pid(daemon_type, daemon_index)
        if pid == 0:
            logging.info("Server type={} index={} already stopped".format(
                daemon_type, daemon_index))
            return
        logging.info("Stopping server type={} index={} PID={}".format(
            daemon_type, daemon_index, pid))
        # Kill the process.
        os.kill(pid, signal.SIGTERM)
        # Wait for process to stop.
        while True:
            try:
                logging.info("Waiting for server type={} index={} PID={} to stop...".format(
                    daemon_type, daemon_index, pid))
                time.sleep(0.5)
                os.kill(pid, 0)
            except OSError as err:
                if err.errno == errno.ESRCH:
                    return

    def create(self):
        server_counts = self.options.replication_factor
        self.set_master_addresses(server_counts)

        if os.path.isdir(self.options.cluster_base_dir):
            raise RuntimeError("Found cluster data at {}, cannot create new cluster...".format(
                self.options.cluster_base_dir))
        os.makedirs(self.options.cluster_base_dir)

        for t in ClusterOptions.DAEMON_TYPES:
            for i in range(1, server_counts + 1):
                pid = self.get_pid(t, i)
                if pid > 0:
                    logging.info("Server type={} index={} is running on PID={}".format(t, i, pid))
                else:
                    self.start_daemon(t, i)

    def add_node(self):
        self.set_master_addresses(self.get_number_servers("master"))
        daemon_type = "tserver"
        num_servers = self.get_number_servers(daemon_type)
        self.start_daemon(daemon_type, num_servers + 1)

    def remove_node(self):
        daemon_type = "tserver"
        daemon_index = self.args.node_id
        logging.info("Removing server type={} index={}".format(daemon_type, daemon_index))
        self.stop_daemon(daemon_type, daemon_index)

    def status(self):
        for t in ClusterOptions.DAEMON_TYPES:
            num_servers = self.get_number_servers(t)
            for i in range(1, num_servers + 1):
                pid = self.get_pid(t, i)
                if pid == 0:
                    logging.info("Server type={} index={} is not running".format(t, i))
                else:
                    logging.info("Server type={} index={} is running on PID={}".format(t, i, pid))

    def destroy(self):
        # Stop all the daemons.
        for t in ["master", "tserver"]:
            num_servers = self.get_number_servers(t)
            for i in range(1, num_servers + 1):
                self.stop_daemon(t, i)
        # Remove the top-level directory.
        top_level = self.options.cluster_base_dir
        if os.path.exists(top_level) and os.path.isdir(top_level):
            logging.info("Removing base directory: {}".format(top_level))
            shutil.rmtree(self.options.cluster_base_dir)


if __name__ == "__main__":
    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s: %(message)s")

    ClusterControl().run()
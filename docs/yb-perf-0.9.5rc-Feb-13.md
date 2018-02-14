# Setup
Replication factor (num nodes): 3
Cluster node type: n1-standard-16
CPU type: Intel(R) Xeon(R) CPU @ 2.30GHz
specs: {"memory" : "60GB", "vCPUs" : "16", "numDisks" : "2", "diskSize" : "375GB", "diskType" : "SSD"}

# Performance Summary:

## Workload CassandraKeyValue with 256 writers and 0 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Read latency, ms/op            | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Write throughput, ops/sec      | 99366.97  | 96127.34  | 101478.62 | 1555.17   | 99391.40  | 96127.34  | 96162.20  | 96848.58  | 101192.79 | 101464.57 | 101478.62 |
| Write latency, ms/op           | 2.58      | 2.52      | 2.66      | 0.04      | 2.58      | 2.52      | 2.52      | 2.53      | 2.64      | 2.66      | 2.66      |
| Load tester CPU, user, %       | 20.50     | 4.90      | 25.20     | 3.00      | 20.80     | 4.90      | 14.33     | 20.09     | 22        | 23.44     | 25.20     |
| Load tester CPU, system, %     | 6.51      | 0.40      | 8.70      | 1.23      | 6.60      | 0.40      | 4.17      | 6.26      | 7.50      | 8.24      | 8.70      |
| Cluster node CPU, user, %      | 59.76     | 1.70      | 64.10     | 11.00     | 62.05     | 1.70      | 44.13     | 60.17     | 63.63     | 63.81     | 64.10     |
| Cluster node CPU, system, %    | 16.87     | 1         | 18.80     | 2.94      | 17.45     | 1         | 14.50     | 16.70     | 18.10     | 18.70     | 18.80     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload CassandraKeyValue with 192 writers and 16 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 23272.02  | 21966.13  | 23983.06  | 438.85    | 23267.66  | 21966.13  | 21966.13  | 22833.11  | 23754.47  | 23983.06  | 23983.06  |
| Read latency, ms/op            | 0.69      | 0.67      | 0.73      | 0.01      | 0.69      | 0.67      | 0.67      | 0.67      | 0.70      | 0.73      | 0.73      |
| Write throughput, ops/sec      | 78600.94  | 77501.29  | 80100.93  | 787.69    | 78564.68  | 77501.29  | 77501.29  | 77567.06  | 79818.39  | 80100.93  | 80100.93  |
| Write latency, ms/op           | 2.44      | 2.40      | 2.48      | 0.02      | 2.44      | 2.40      | 2.40      | 2.41      | 2.47      | 2.48      | 2.48      |
| Load tester CPU, user, %       | 21.52     | 18.50     | 24.10     | 0.94      | 21.50     | 18.50     | 18.89     | 20.86     | 22.24     | 23.64     | 24.10     |
| Load tester CPU, system, %     | 6.63      | 0.50      | 8.70      | 1.23      | 6.70      | 0.50      | 4.08      | 6.53      | 7.18      | 8.63      | 8.70      |
| Cluster node CPU, user, %      | 60.65     | 1.60      | 65        | 11.20     | 63.30     | 1.60      | 42.25     | 60.14     | 64.46     | 64.80     | 65        |
| Cluster node CPU, system, %    | 16.21     | 0.80      | 18.30     | 2.82      | 16.80     | 0.80      | 14.10     | 16.01     | 17.30     | 17.41     | 18.30     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload CassandraKeyValue with 128 writers and 64 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 79914.91  | 77776.12  | 81807.71  | 1235.22   | 80221.67  | 77776.12  | 77776.12  | 78326.41  | 81704.79  | 81807.71  | 81807.71  |
| Read latency, ms/op            | 0.80      | 0.78      | 0.82      | 0.01      | 0.80      | 0.78      | 0.78      | 0.78      | 0.82      | 0.82      | 0.82      |
| Write throughput, ops/sec      | 47148.21  | 44196.03  | 48441.79  | 1051.87   | 47554.87  | 44196.03  | 44196.03  | 45278.22  | 48275.53  | 48441.79  | 48441.79  |
| Write latency, ms/op           | 2.72      | 2.64      | 2.90      | 0.06      | 2.69      | 2.64      | 2.64      | 2.65      | 2.83      | 2.90      | 2.90      |
| Load tester CPU, user, %       | 26.29     | 25.40     | 30.70     | 1.10      | 25.80     | 25.40     | 25.46     | 25.52     | 27.92     | 29.14     | 30.70     |
| Load tester CPU, system, %     | 7.98      | 7         | 9.80      | 0.60      | 7.80      | 7         | 7.42      | 7.70      | 9.30      | 9.74      | 9.80      |
| Cluster node CPU, user, %      | 66.44     | 39.70     | 69.10     | 4.91      | 67.40     | 39.70     | 65.58     | 66.10     | 68.36     | 68.60     | 69.10     |
| Cluster node CPU, system, %    | 14.38     | 10.40     | 15.30     | 0.74      | 14.40     | 10.40     | 14        | 14.10     | 14.86     | 15        | 15.30     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload CassandraKeyValue with 64 writers and 128 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 122754.63 | 119765.78 | 125236.96 | 2038.87   | 121961.30 | 119765.78 | 119765.78 | 120173.18 | 125044.05 | 125236.96 | 125236.96 |
| Read latency, ms/op            | 1.04      | 1.02      | 1.07      | 0.02      | 1.05      | 1.02      | 1.02      | 1.02      | 1.06      | 1.07      | 1.07      |
| Write throughput, ops/sec      | 22612.50  | 22317.48  | 22954.84  | 252.80    | 22569.02  | 22317.48  | 22317.48  | 22321.28  | 22947.05  | 22954.84  | 22954.84  |
| Write latency, ms/op           | 2.83      | 2.79      | 2.87      | 0.03      | 2.84      | 2.79      | 2.79      | 2.79      | 2.87      | 2.87      | 2.87      |
| Load tester CPU, user, %       | 28.71     | 27.60     | 44.50     | 2.95      | 28.10     | 27.60     | 27.66     | 27.80     | 28.78     | 35.32     | 44.50     |
| Load tester CPU, system, %     | 8.30      | 7.80      | 10        | 0.50      | 8.10      | 7.80      | 7.80      | 7.90      | 8.88      | 9.82      | 10        |
| Cluster node CPU, user, %      | 68.73     | 61.10     | 70.50     | 1.45      | 69        | 61.10     | 67.30     | 67.70     | 69.86     | 70.13     | 70.50     |
| Cluster node CPU, system, %    | 13.38     | 12.60     | 14.80     | 0.52      | 13.20     | 12.60     | 12.74     | 12.90     | 14.26     | 14.40     | 14.80     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload CassandraKeyValue with 0 writers and 256 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 201614.72 | 200307.26 | 202889.64 | 714.00    | 201504.84 | 200307.26 | 200307.26 | 200503.16 | 202425.52 | 202889.64 | 202889.64 |
| Read latency, ms/op            | 1.27      | 1.26      | 1.28      | 0.00      | 1.27      | 1.26      | 1.26      | 1.26      | 1.28      | 1.28      | 1.28      |
| Write throughput, ops/sec      | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Write latency, ms/op           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Load tester CPU, user, %       | 32.34     | 3.20      | 37.50     | 8.31      | 35.60     | 3.20      | 10.96     | 15.92     | 35.94     | 36.38     | 37.50     |
| Load tester CPU, system, %     | 8.63      | 0.30      | 10.70     | 2.03      | 9.30      | 0.30      | 3.10      | 5.86      | 9.72      | 10.22     | 10.70     |
| Cluster node CPU, user, %      | 61.93     | 0.90      | 68.50     | 13.77     | 66.90     | 0.92      | 25.30     | 49.52     | 67.80     | 68.10     | 68.48     |
| Cluster node CPU, system, %    | 7.58      | 0.60      | 20.90     | 3.79      | 6.50      | 0.61      | 5.03      | 6.40      | 11.36     | 20.20     | 20.89     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

## Workload RedisKeyValue with 256 writers and 0 readers: 
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Read latency, ms/op            | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Write throughput, ops/sec      | 92456.21  | 89881.85  | 93587.61  | 1142.77   | 92769.20  | 89881.85  | 89907.11  | 90175.39  | 93580.16  | 93585.45  | 93587.61  |
| Write latency, ms/op           | 2.77      | 2.73      | 2.85      | 0.04      | 2.76      | 2.73      | 2.73      | 2.74      | 2.84      | 2.85      | 2.85      |
| Load tester CPU, user, %       | 3.37      | 2.90      | 4.10      | 0.30      | 3.30      | 2.90      | 2.90      | 2.93      | 3.70      | 3.90      | 4.10      |
| Load tester CPU, system, %     | 4.79      | 4.40      | 6.50      | 0.36      | 4.70      | 4.40      | 4.46      | 4.50      | 5.07      | 5.59      | 6.50      |
| Cluster node CPU, user, %      | 59.51     | 57.30     | 61.30     | 0.72      | 59.50     | 57.30     | 58.38     | 58.67     | 60.33     | 60.91     | 61.30     |
| Cluster node CPU, system, %    | 23.11     | 22.30     | 24.10     | 0.36      | 23        | 22.30     | 22.60     | 22.67     | 23.60     | 23.80     | 24.10     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisKeyValue with 192 writers and 16 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 15746.55  | 14798.52  | 16604.97  | 312.01    | 15712.88  | 14798.52  | 14992.74  | 15523.80  | 16152.28  | 16487.20  | 16604.97  |
| Read latency, ms/op            | 1.02      | 0.96      | 1.08      | 0.02      | 1.02      | 0.96      | 0.97      | 0.99      | 1.03      | 1.07      | 1.08      |
| Write throughput, ops/sec      | 74182.39  | 68805.92  | 75735.01  | 1952.70   | 74777.62  | 68805.92  | 69067.63  | 69785.63  | 75707.92  | 75727.43  | 75735.01  |
| Write latency, ms/op           | 2.59      | 2.53      | 2.79      | 0.07      | 2.57      | 2.53      | 2.53      | 2.54      | 2.75      | 2.78      | 2.79      |
| Load tester CPU, user, %       | 3.22      | 2.80      | 4         | 0.27      | 3.20      | 2.80      | 2.86      | 2.90      | 3.60      | 3.87      | 4         |
| Load tester CPU, system, %     | 4.59      | 3.90      | 6         | 0.45      | 4.50      | 3.90      | 3.96      | 4.10      | 5.07      | 5.74      | 6         |
| Cluster node CPU, user, %      | 58.81     | 56.10     | 60.50     | 1.10      | 58.80     | 56.10     | 56.77     | 57.57     | 60.30     | 60.41     | 60.50     |
| Cluster node CPU, system, %    | 22.72     | 21.70     | 23.50     | 0.42      | 22.70     | 21.70     | 21.88     | 22.20     | 23.30     | 23.40     | 23.50     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisKeyValue with 128 writers and 64 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 59762.40  | 53457.38  | 64676.29  | 2188.75   | 59201.17  | 53457.38  | 54758.38  | 57856.00  | 62421.86  | 64291.83  | 64676.29  |
| Read latency, ms/op            | 1.07      | 0.99      | 1.20      | 0.04      | 1.08      | 0.99      | 1.00      | 1.03      | 1.11      | 1.17      | 1.20      |
| Write throughput, ops/sec      | 43200.49  | 33112.89  | 47904.65  | 5446.83   | 46061.52  | 33112.89  | 33145.46  | 33448.36  | 47757.41  | 47879.56  | 47904.65  |
| Write latency, ms/op           | 3.01      | 2.67      | 3.87      | 0.43      | 2.78      | 2.67      | 2.67      | 2.68      | 3.83      | 3.86      | 3.87      |
| Load tester CPU, user, %       | 4.05      | 3.40      | 5.40      | 0.44      | 4.10      | 3.40      | 3.40      | 3.50      | 4.71      | 5.07      | 5.40      |
| Load tester CPU, system, %     | 5.38      | 4.40      | 7         | 0.59      | 5.40      | 4.40      | 4.46      | 4.50      | 6.41      | 6.67      | 7         |
| Cluster node CPU, user, %      | 60.06     | 56.10     | 62.90     | 1.40      | 60.10     | 56.10     | 57.28     | 57.87     | 61.73     | 62.43     | 62.90     |
| Cluster node CPU, system, %    | 21.31     | 19.10     | 22.50     | 0.89      | 21.50     | 19.10     | 19.40     | 19.80     | 22.10     | 22.40     | 22.50     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisKeyValue with 64 writers and 128 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 112991.15 | 111322.60 | 116438.16 | 1803.87   | 112046.65 | 111322.60 | 111341.83 | 111387.75 | 116353.19 | 116413.58 | 116438.16 |
| Read latency, ms/op            | 1.13      | 1.10      | 1.15      | 0.02      | 1.14      | 1.10      | 1.10      | 1.10      | 1.15      | 1.15      | 1.15      |
| Write throughput, ops/sec      | 23425.51  | 23122.10  | 23617.57  | 121.56    | 23412.04  | 23122.10  | 23158.06  | 23263.31  | 23589.86  | 23615.32  | 23617.57  |
| Write latency, ms/op           | 2.73      | 2.71      | 2.77      | 0.01      | 2.73      | 2.71      | 2.71      | 2.71      | 2.75      | 2.76      | 2.77      |
| Load tester CPU, user, %       | 5.41      | 5.10      | 6.10      | 0.24      | 5.30      | 5.10      | 5.10      | 5.13      | 5.77      | 5.97      | 6.10      |
| Load tester CPU, system, %     | 7.52      | 7.20      | 8.70      | 0.41      | 7.40      | 7.20      | 7.20      | 7.20      | 8.20      | 8.50      | 8.70      |
| Cluster node CPU, user, %      | 61.17     | 60        | 61.90     | 0.41      | 61.30     | 60        | 60.48     | 60.60     | 61.70     | 61.80     | 61.90     |
| Cluster node CPU, system, %    | 20.99     | 20.30     | 21.60     | 0.31      | 21        | 20.30     | 20.50     | 20.60     | 21.40     | 21.50     | 21.60     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisKeyValue with 0 writers and 256 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 214841.72 | 213904.27 | 215777.03 | 449.18    | 214863.35 | 213904.27 | 213983.57 | 214261.27 | 215407.97 | 215696.97 | 215777.03 |
| Read latency, ms/op            | 1.19      | 1.19      | 1.20      | 0.00      | 1.19      | 1.19      | 1.19      | 1.19      | 1.19      | 1.20      | 1.20      |
| Write throughput, ops/sec      | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Write latency, ms/op           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Load tester CPU, user, %       | 8.26      | 2.40      | 8.90      | 1.56      | 8.70      | 2.40      | 2.62      | 6.95      | 8.90      | 8.90      | 8.90      |
| Load tester CPU, system, %     | 12.11     | 3.80      | 13.20     | 2.31      | 12.80     | 3.80      | 3.88      | 9.85      | 13        | 13.05     | 13.20     |
| Cluster node CPU, user, %      | 60.76     | 49.30     | 62.50     | 2.77      | 61.80     | 49.31     | 51.40     | 60.50     | 62.10     | 62.28     | 62.50     |
| Cluster node CPU, system, %    | 17.94     | 16.70     | 23.80     | 1.52      | 17.40     | 16.70     | 17        | 17.03     | 18.30     | 22.94     | 23.80     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisPipelinedKeyValue with 24 writers and 0 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Read latency, ms/op            | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Write throughput, ops/sec      | 566123.94 | 542334.20 | 621498.05 | 17989.81  | 561921.60 | 542334.20 | 544247.73 | 548784.51 | 592584.80 | 614453.05 | 621498.05 |
| Write latency, ms/op           | 20.50     | 18.60     | 21.39     | 0.65      | 20.64     | 18.60     | 18.83     | 19.54     | 21.16     | 21.32     | 21.39     |
| Load tester CPU, user, %       | 7.82      | 7.20      | 8.40      | 0.29      | 7.80      | 7.20      | 7.26      | 7.42      | 8.20      | 8.34      | 8.40      |
| Load tester CPU, system, %     | 0.37      | 0.30      | 1         | 0.13      | 0.40      | 0.30      | 0.30      | 0.30      | 0.40      | 0.64      | 1         |
| Cluster node CPU, user, %      | 65.54     | 60.40     | 71.60     | 2.96      | 66.10     | 60.40     | 60.77     | 61.30     | 69.06     | 69.62     | 71.60     |
| Cluster node CPU, system, %    | 8.63      | 8.10      | 9.30      | 0.27      | 8.60      | 8.10      | 8.27      | 8.30      | 9         | 9.13      | 9.30      |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisPipelinedKeyValue with 14 writers and 3 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 84996.20  | 69590.97  | 105784.05 | 10238.89  | 83938.67  | 69590.97  | 70190.77  | 72340.37  | 100734.43 | 104708.96 | 105784.05 |
| Read latency, ms/op            | 17.28     | 13.58     | 21.01     | 2.10      | 17.25     | 13.58     | 13.73     | 14.31     | 20.08     | 20.80     | 21.01     |
| Write throughput, ops/sec      | 311772.26 | 251467.50 | 428633.89 | 59385.15  | 285713.69 | 251467.50 | 251792.38 | 253116.04 | 422988.02 | 427958.24 | 428633.89 |
| Write latency, ms/op           | 22.42     | 15.62     | 27.13     | 3.84      | 23.73     | 15.62     | 15.64     | 15.83     | 26.90     | 27.09     | 27.13     |
| Load tester CPU, user, %       | 5.36      | 4.20      | 6.70      | 0.77      | 5.20      | 4.20      | 4.26      | 4.32      | 6.48      | 6.64      | 6.70      |
| Load tester CPU, system, %     | 0.25      | 0.20      | 0.30      | 0.05      | 0.30      | 0.20      | 0.20      | 0.20      | 0.30      | 0.30      | 0.30      |
| Cluster node CPU, user, %      | 67.23     | 55.20     | 75        | 4.52      | 67.90     | 55.20     | 59.17     | 60.80     | 72.70     | 73.68     | 75        |
| Cluster node CPU, system, %    | 8.81      | 6.30      | 12.30     | 1.68      | 8.40      | 6.30      | 6.50      | 6.74      | 11.06     | 11.33     | 12.30     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisPipelinedKeyValue with 10 writers and 6 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 133714.57 | 125184.69 | 145178.21 | 4136.00   | 133280.49 | 125184.69 | 125934.10 | 129032.64 | 139378.68 | 143803.08 | 145178.21 |
| Read latency, ms/op            | 21.84     | 20.08     | 23.35     | 0.68      | 21.88     | 20.08     | 20.28     | 20.92     | 22.64     | 23.22     | 23.35     |
| Write throughput, ops/sec      | 310023.18 | 264463.98 | 360847.90 | 30138.79  | 306100.78 | 264463.98 | 265539.46 | 271067.11 | 354247.92 | 359297.33 | 360847.90 |
| Write latency, ms/op           | 15.52     | 13.13     | 18.13     | 1.54      | 15.61     | 13.13     | 13.19     | 13.38     | 17.67     | 18.05     | 18.13     |
| Load tester CPU, user, %       | 5.84      | 5.30      | 6.60      | 0.41      | 5.70      | 5.30      | 5.36      | 5.40      | 6.38      | 6.54      | 6.60      |
| Load tester CPU, system, %     | 0.25      | 0.20      | 0.30      | 0.05      | 0.30      | 0.20      | 0.20      | 0.20      | 0.30      | 0.30      | 0.30      |
| Cluster node CPU, user, %      | 65.42     | 58.70     | 70.20     | 2.96      | 66        | 58.70     | 60.37     | 61.08     | 69.36     | 69.76     | 70.20     |
| Cluster node CPU, system, %    | 11.52     | 10.40     | 12.90     | 0.56      | 11.50     | 10.40     | 10.57     | 10.74     | 12.46     | 12.60     | 12.90     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisPipelinedKeyValue with 4 writers and 12 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 155186.22 | 145181.54 | 164775.35 | 6392.86   | 156528.21 | 145181.54 | 145656.70 | 147281.76 | 163825.95 | 164700.17 | 164775.35 |
| Read latency, ms/op            | 38.10     | 35.81     | 40.63     | 1.59      | 37.70     | 35.81     | 35.84     | 36.03     | 40.11     | 40.52     | 40.63     |
| Write throughput, ops/sec      | 175429.28 | 140281.19 | 194071.40 | 17773.80  | 184523.45 | 140281.19 | 142455.16 | 149226.41 | 191872.91 | 193521.79 | 194071.40 |
| Write latency, ms/op           | 10.77     | 9.54      | 13.45     | 1.25      | 10.09     | 9.54      | 9.57      | 9.68      | 12.63     | 13.25     | 13.45     |
| Load tester CPU, user, %       | 4.13      | 3.80      | 4.40      | 0.19      | 4.20      | 3.80      | 3.80      | 3.80      | 4.30      | 4.40      | 4.40      |
| Load tester CPU, system, %     | 0.21      | 0.20      | 0.60      | 0.07      | 0.20      | 0.20      | 0.20      | 0.20      | 0.20      | 0.36      | 0.60      |
| Cluster node CPU, user, %      | 56.98     | 51        | 64.60     | 4.08      | 55.70     | 51        | 51.54     | 52.48     | 63.82     | 64.13     | 64.60     |
| Cluster node CPU, system, %    | 12.71     | 11.30     | 13.80     | 0.63      | 12.80     | 11.30     | 11.40     | 11.74     | 13.50     | 13.70     | 13.80     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

## Workload RedisPipelinedKeyValue with 0 writers and 16 readers: 
```
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Metric                         | mean      | min       | max       | std.dev   | median    | 1%        | 5%        | 10%       | 90%       | 95%       | 99%       |
| Read throughput, ops/sec       | 231742.87 | 229867.84 | 233765.93 | 1084.56   | 231667.88 | 229867.84 | 229892.83 | 230266.98 | 233417.73 | 233715.83 | 233765.93 |
| Read latency, ms/op            | 33.93     | 33.64     | 34.21     | 0.16      | 33.91     | 33.64     | 33.66     | 33.72     | 34.12     | 34.19     | 34.21     |
| Write throughput, ops/sec      | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Write latency, ms/op           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| Load tester CPU, user, %       | 2.15      | 2.10      | 3         | 0.17      | 2.10      | 2.10      | 2.10      | 2.10      | 2.20      | 2.56      | 3         |
| Load tester CPU, system, %     | 0.14      | 0.10      | 0.60      | 0.12      | 0.10      | 0.10      | 0.10      | 0.10      | 0.20      | 0.54      | 0.60      |
| Cluster node CPU, user, %      | 34.06     | 30.70     | 41.80     | 2.33      | 34.20     | 30.70     | 30.90     | 31.01     | 36.39     | 37.50     | 41.80     |
| Cluster node CPU, system, %    | 11.29     | 10.70     | 11.60     | 0.20      | 11.30     | 10.70     | 11        | 11.01     | 11.50     | 11.60     | 11.60     |
+--------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```


# YCSB run info:
```
+--------------+----------------------+--------------------+--------------------+--------------------+
| Workload     | Throughput (ops/sec) | Op Type            | Avg Latency (us)   | 99th% Latency (us) |
| workloada    | 105895.18            | READ               | 1212.72            | 2993               |
|              |                      | UPDATE             | 3456.98            | 8711               |
|              |                      |                    |                    |                    |
| workloadb    | 110937.31            | READ               | 2134.25            | 4783               |
|              |                      | UPDATE             | 4068.31            | 8383               |
|              |                      |                    |                    |                    |
| workloadc    | 118690.14            | READ               | 2080.24            | 4491               |
|              |                      |                    |                    |                    |
| workloadd    | 115248.53            | READ               | 2037.84            | 4223               |
|              |                      | INSERT             | 4155.01            | 8991               |
|              |                      |                    |                    |                    |
| workloade    | 8465.72              | INSERT             | 23039.98           | 87935              |
|              |                      | SCAN               | 29892.0            | 103615             |
|              |                      |                    |                    |                    |
| workloadf    | 69516.88             | READ               | 1531.78            | 3853               |
|              |                      | READ-MODIFY-WRITE  | 5659.65            | 14063              |
|              |                      | UPDATE             | 4124.91            | 11535              |
|              |                      |                    |                    |                    |
+--------------+----------------------+--------------------+--------------------+--------------------+
```
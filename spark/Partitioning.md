check the size of partition of RDD using - 

in scala :
`RDD.partitions.size`

in python :
`RDD.getNumPartitions()`


By default , Spark will decide parallelism but to specify custom level of parallelism, a 2nd parameter can be specified
while performing transformation/aggregate operation as -

`file = sc.textFile("xyz.txt",10)   => 10 partitions`
`file.flatMap(x => x.split(" ")).map( x => (x,1)).reduceByKey( (x,y) => x +y,4)`


to perform partitioning out side the context of grouping and aggregation, spark provides `repartition()` function.
More optimized version of `repartition()` is `coalesce()`




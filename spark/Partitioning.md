- Check the size of partition of RDD using - 

        in scala :
        `RDD.partitions.size`
        
        in python :
        `RDD.getNumPartitions()`


-By default , Spark will decide parallelism but to specify custom level of parallelism, a 2nd parameter can be specified
  while performing transformation/aggregate operation as -

        `file = sc.textFile("xyz.txt",10)   => 10 partitions`
        `file.flatMap(x => x.split(" ")).map( x => (x,1)).reduceByKey( (x,y) => x +y,4)`


- To perform partitioning out side the context of grouping and aggregation, spark provides `repartition()` function.
More optimized version of `repartition()` is `coalesce()`


- Paritioning is useful only when dataset is reused multiple times in key oriented operations such as `join`

- Another way custom paritioner can be defined using partitionBy() method and passing a new HashPartitioner(Int) to that method.
  ```
  import org.apache.spark.HashPartitioner
  
  val map1 = sc.textFile("moby.txt").flatMap( x => x.split(" ")).map(x=>(x,1))
  val PartMap = map1.partitionBy(new HashPartitioner(100))
  
  ```
  




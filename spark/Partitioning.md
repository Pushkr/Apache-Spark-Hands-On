- Check the size of partition of RDD using - 

        in scala :
        `RDD.partitions.size`
        
        in python :
        `RDD.getNumPartitions()`

- to see elements in each partition (using python) 
        ` RDD.glom().collect()`

-By default , Spark will decide parallelism but to specify custom level of parallelism, a 2nd parameter can be specified
  while performing transformation/aggregate operation as -

        `file = sc.textFile("xyz.txt",10)   => 10 partitions`
        `file.flatMap(x => x.split(" ")).map( x => (x,1)).reduceByKey( (x,y) => x +y,4)`


- To perform partitioning out side the context of grouping and aggregation, spark provides `repartition()` function.
More optimized version of `repartition()` is `coalesce()`


- Paritioning is useful only when dataset is reused multiple times in key oriented operations such as `join`

- Another way custom paritioner for **paired RDDS** can be defined using partitionBy() method and passing a new **HashPartitioner(Int)/RangePartitioner** to that method.
  
  in Scala: 
  ```
  import org.apache.spark.HashPartitioner
  
  val map1 = sc.textFile("moby.txt").flatMap( x => x.split(" ")).map(x=>(x,1))
  val PartMap = map1.partitionBy(new HashPartitioner(100)).persist()
  ```
  
  in Python :
  
  ` val PartMap = map1.partitionBy(100).persist()`
  
  _since paritionBy is transformation operation, user persist() after partitionBy, otherwise each time_
  
  _rdd is referenced, it will get partitioned repeatedly. This will negate the effect of partitionBy_
 
  
  for following operations results in partitioner gets set on output RDD automatically -
        - join
        - cogroup
        - groupWith()
        - leftOuterJoin()
        - rightOuterJoin()
        - flatMapValues() - if parent RDD has partitioner
        - filter() - if parent RDD has partitioner
        - groupByKey()
        - sort()
        - reduceByKey()
        - combineByKey()
        - mapValues()  - if parent RDD has partitioner
        - partitionBy()
        
- To maximize the potential for partiioning related optimizations, always use mapValues() or flatMapValues() whenever 
  there is no change in elements keys

- To further customize partition, function can be defined , for e.g. to parition

```
        def hash_part(url)
                return(urlparse.urlparse(url).netloc)
         
        RDD.partitionBy(20,hash_part)
``` 




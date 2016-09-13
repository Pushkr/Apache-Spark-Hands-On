## Creating Key-Value Pair
- while loading data from csv/json/text file, key and value pairs can directly formed.
- Using map() function, k-v pair can be formed 

##Transformations
###Aggregate Operations

- reduceByKey() 
- mapValues(function)
- flatMapValues(function)
- keys()
- combineByKey(createCombiner,mergeValue,mergeCombiner,paritioner)
      - createComniber => is a function that is executed when a new value of key is encountered
      - mergeValue => is a function that is executed when existing value of key is encounted
      - mergeCombiner => is a combiner function that combines accumulators from different partitions.
      - partitioner => may be HashPartitioner/RangePartitioner/custom Partitioner function, I am not sure yet.
      
  - foldByKey() - same as reduceByKey except here initial value can be specified.


###Grouping

- groupWith()
- groupByKey() - will group RDD elements accoridng to key. Output is in [k,Iterable[v]] format
- cogroup() - when multiple RDDs have similar keys, they can be grouped using this function.

### Joins 

- join()
- leftOuterJoin()
- rightOuterJoin()
 


###Sorting
- sortByKey(ascending = True, numPartitions= None,keyfunc) -
    by default keys are in ascending order 


## Actions
- collectAsMap() 
- countByKey()
- lookup(key)

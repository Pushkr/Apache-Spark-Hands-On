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
- aggregateByKey(zeroValue)(seqOp, combOp, [numTasks])- 
      - zeroValue => initial value for aggregation
      - seqop => operates on each row 
      - combOp => Operates on each reducer output
      
   for e.g.
   Assume , there is a dataset that contains (userID, rating) pair. To calculate average rating by each user, I used following
   script - 

```
   user_sumcnt = user_rating.aggregateByKey((0,0.0),\
    (lambda x, y: (x[0]+y,x[1]+1)),
    (lambda r1,r2 : (r1[0]+r2[0],r1[1]+r2[1]))) 
    
```
      here -
      zeroValue = (0,0.0) = this corresponds to (sumOfRatings = 0 , totalNumberOfRatings = 0.0) 
      
      seqOp = lambda x,y : x[0]+y,x[1]+1 => this function operates on VALUE part of each row 
      (like reduceByKey) and produces (userId,(sumOfRatings,CountOfRatings)) pair. x[0] is 
      0 initially, y is value of entire row i.e. in this case rating and x[1] is just an count 
      to keep track of how many ratings a user has. It increaments everytime a rating for user is found
      
      combOp = lambda r1,r2 : (r1[0]+r2[0],r1[1]+r2[1]) 
      this just sums up results from multiple reducers into one. For e.g reducer1 and reducer2 may have output 
      pair for userID = 1, so this combOp will just adds  sumOfRatings from reducer1 to sumOfRatings from
      reducer2 and CountOfRatings from reducer1 to CountOfRatings from reducer2 producing final output
      
      


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

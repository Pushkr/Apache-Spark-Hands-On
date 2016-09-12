Basic commands - 

## Load text file
`val lines = sc.textFile("moby.txt")`

## Transformation - 

### One RDD transformations
  - map() -  
    
     ` val newline = lines.map(line => (line, "length of line is " + line.length()))`
  
  - filter() -
  
     ` val newline = lines.filter(line => line.length() > 0)`

  - flatMap() - flatMap is useful in scenarios where multiple output from transformation is expected. In this case,
                flatMap will combine output from multiple iterators and present as one. For example, to split a block 
                of text by words, all the lines can be passed thru flatMap and using split(" ") method. Instead of 
                returning iterator for each line , flatmap will return one single iterator containing all the words.

     ` val words = lines.flatMap(line => line.split(" ")) `
  - sample(withReplcaement,fraction,[seed]) - 
                sample RDD with or without replacement. 
  
     ` rdd.sample(false,0.5)`
  
  - distinct() - This operation is very resouce expensive.
    ` val newRDD = oldRDD.distinct() `

###Two RDD transformations 
- union() - join two RDDs. This will not remove duplicates.
        ` val newRDD = oldRDD1.union(oldRDD2) `

- intersection() - This will remove duplicates.
        ` val newRDD = oldRDD1.intersection(oldRDD2)`

- substract()
  
- cartesian() 
  
  
    
## Actions -
### ONE RDD ACTIONS
  - reduce(func) - performd operation on two elements on same RDD and returns element of same type.
    ` val sum = oldRDD.reduce( (x,y) => x + y) ` 
  
  - fold(zeroValue)(func) - same as reduce except it accepts a 'zero value' to be used for initial call on each partition.
  
  - aggregrate(zeroValue)(seqFunc,comboFunc) - 
    As oppose to reduce and fold, aggregate doesnt not require to have same return type as elements in RDD it operates on. 
    The aggregate function allows the user to apply two different reduce functions to the RDD. The first reduce function is applied within each partition to reduce the data within each partition into a single result. The second reduce function is used to combine the different reduced results of all partitions together to arrive at one final result. The ability to have two separate reduce functions for intra partition versus across partition reducing adds a lot of flexibility. For example the first reduce function can be the max function and the second one can be the sum function. The user also specifies an initial value

     aggregate() needs - 
                - inital value (like fold() )
                - one function to operate on elements on RDD with accumulator
                - 2nd function to combine outputs from accumulators.
      ```
                  val z = sc.parallelize(List(1,2,3,4,5,6,7,8,9),2)  /* partiotions = 2 */ 
      ```
      since partitions = 2 , this list will be split in two as partition 0 = [1,2,3,4] and partition 1 = [5,6,7,8,9]
                  
      to find average of this list, use following aggregate 
      ```
                   val result = z.aggregate((0,0))(
                                  (x,y) => (x._1 + y,x._2 + 1),
                                  (a,b) => (a._1 + b._1,a._2+b._2) )
                  val avg = result._1/result._2
      ```
      explaination - function `(x,y) => (x._1 + y,x._2 + 1)` will operate on each element in individual partitions separately.
      (0,0) is initial value of x so x._1 = 0 and x._2 = 0
      first iteration will operate on [(0,0),1] producing  0+1,0+1 = (1,1) 
      2nd iteration will operate on [(1,1),2] producing 1+2,1 +1 = (3,2)
      3rd iteration will operate on [(3,2),3] producing 3+3,2+1 = (6,3)
      and at last , [(6,3),4] will produce  6+6,3+1 = (10,4)
      similarly output of 2nd partition will be = (35,5) 
      function `(a,b) => (a._1 + b._1,a._2+b._2)' will operate on (10,4) and (35,5) producing result = (45,9)
  
  - foreach(func) - applies provided function to each element of RDD
  
  - count() - returns number of elements in RDD
  
  - countByValue()  - returns map of unique value to its count in RDD
  
  - first() - returns first element of RDD
  
  - take(n)  - returns n number of elements from RDD.
  
  - top(n) - if RDD is ordered, top n elements will be returned.
  
  - collect() - dont use this on large cluster unless driver machine has enough capability to store all the data. collect()
                method will retrieve all data to driver program
  
  - takeSample(withReplacement,num,[seed]) - returns random sample of elements
   
  - takeOrdered(numOfElementToReturn)(ordering function) - returns num elements based on ordering function
  





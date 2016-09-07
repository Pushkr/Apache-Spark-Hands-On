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
  - reduce() - performd operation on two elements on same RDD and returns element of same type.
    ` val sum = oldRDD.reduce( (x,y) => x + y) ` 
  
  - fold() - same as reduce except it accepts a 'zero value' to be used for initial call on each partition.
  
  - aggregrate() - As oppose to reduce and fold, aggregate doesnt not require to have same return type as elements in RDD
                   it operates on. 
                  The aggregate function allows the user to apply two different reduce functions to the RDD. The first reduce function is applied within each partition to reduce the data within each partition into a single result. The second reduce function is used to combine the different reduced results of all partitions together to arrive at one final result. The ability to have two separate reduce functions for intra partition versus across partition reducing adds a lot of flexibility. For example the first reduce function can be the max function and the second one can be the sum function. The user also specifies an initial value

                  aggregate() needs - 
                    - inital value (like fold() )
                    - one function to operate on elements on RDD with accumulator
                    - 2nd function to combine outputs from accumulators.
  
  - count()
  
  - first()
  
  - take(n) 
  
  - top(n)
  
  - collect()
  - collect() - dont use this on large cluster unless driver machine has enough capability to store all the data. collect()
                method will retrieve all data on single machine.


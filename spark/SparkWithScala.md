Basic commands - 

1. Load text file
`val lines = sc.textFile("moby.txt")

2. Transformation - 
  - map() -  
    
     ` val newline = lines.map(line => (line, "length of line is " + line.length()))`
  
  - filter() -
  
     ` val newline = lines.filter(line => line.length() > 0)`
  - flatMap() - flatMap is useful in scenarios where multiple output from transformation is expected. In this case, flatMap will combine               output from multiple iterators and present as one. For example, to split a block of text by words, all the lines can be
                passed thru flatMap and using split(" ") method. Instead of returning iterator for each line , flatmap will return one single iterator containing all the words.

              ` val words = lines.flatMap(line => line.split(" ")) `
  

    
3. Actions -
  - count()
  - first()
  - take(n) 
  - top(n)
  - collect() - dont use this on large cluster unless driver machine has enough capability to store all the data. collect()
                method will retrieve all data on single machine.


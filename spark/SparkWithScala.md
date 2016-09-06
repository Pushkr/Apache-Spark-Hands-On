Basic commands - 

1. Load text file
`val lines = sc.textFile("moby.txt")

2. Transformation - 
  - map() -  
    
     ` val newline = lines.map(line => (line, "length of line is " + line.length()))`
  
  - filter() -
  
     ` val newline = lines.filter(line => line.length() > 0)`
    
3. Actions -
  - count()
  - first()
  - take(n) 
  - top(n)
  - collect() - dont use this on large cluster unless driver machine has enough capability to store all the data. collect()
                method will retrieve all data on single machine.


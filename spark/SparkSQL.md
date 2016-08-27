#SparkSQL Cheat Sheet 

##1. Initializing sparkSQL in using python - 
   - sparkSQL can be initalized using HiveContext or SQLContext. 
   - Use `From pyspark.sql import HiveContext,Row` to initalize program.
   - Also, ` From pyspark.sql import SQLContext` can be used if Hive is not installed.
   - Construst a SQL context in pythong using  `hc = HiveContext(sc)`  where is sc is SparkContext
   - To connect SparkSQL to existin Hive installation, copy `hive-site.xml` to Spark's conf directory `($SPARK_HOME/conf)`

##2. Basic Queries using SparkSQL 
  - Use `sql()` method of HiveContext/SQLContext to issue queries.
  for e.g 
           
          `hc.sql("SHOW TABLES").show()`
          `hc.sql("SELECT key,value FROM table1 WHERE key <= 10")` 

##3. Loading data using SparkSQL 
###A. Loading JSON files 
  JSON files can be loaded using jsonFile() method of HiveContext/SQLContext. 
  Also read.json() is alternate method that can be used to load json
      
      ```
      fpath = "file:///home/cloudera/Desktop/json_data/wbank1.json"
      jfile = hc.jsonFile(fpath)` 
      ```
  above json file can be loaded as temporary table which can be queries using SQL commands 
    
      ```
      jfile.registerTempTable("table1")
      data = hc.sql("SELECT * FROM table1 WHERE board_approval_month = "November")
      data.show()
      ```

###B. Loading paraquet files
Loading paraquet files is very much simialr to loading JSON files
    
    `jfile = hc.parquetFile(fpath)`

even paraquet file also can be loaded as temopary table using same `registerTempTable()` method

###C. Saving paraquet files 
incidently, data (i.e. DATAFRAME / SchemaRDD)  from SparkSQL can be saved as paraquet file using -

  ` data.saveAsParaquetFile("xyz.paraquet")`
  
##4. Working on rows  

A simpler way to work on rows is using map() or filter() transformation operations on DATAFRAME/SchemaRDDs.

   ```
   data = hc.sql("SELECT * FROM table1 WHERE board_approval_month = "November")
   data_map = data.map(lambda row : (row['borrower'],row['lendprojectcost'))
   for row in data_map.collect() :
     print(row)
   ```
If a file is loaded using json, select('column name') method can be used.

`data.select('board_approval_month')`

Using python for SparkSQL, a simple `row.columnname`  or `row['column name']`can access columns of a row using its name.,

##5.Reading HIVE table 
And existing hive table can be read simpley using sql() method of HiveContext

   from pyspark.sql import HiveContext,Row
   hc = HiveContext(sc)
   hc.sql("SELECT key,Value FROM table1")

##6. Creating Hive Table 
using a query, a table can be directly created -
```
hc.sql("create table sect_spending as select sector,avg(totalamt) as spending from wbank group by sector order by spending")

or

hc.sql ("CREATE TABLE sample ( ID INT, NAME STRING, AGE INT) 
         ROW FORMAT DELIMITED 
         FIELDS TERMINATED BY ','
         LINES TERMINATED BY '\n'") 
```


##7. Specifying Schema 
### Using reflection - i.e using inferSchema() method
   ```
      people = [Row(name='John',lname='McKay',age=32),Row(name='Thomos',lname='Radagast',age=15)]
      inf_schm = sc.inferSchema(people)
      inf_schm.registerTempTable("people")
   ```
### Programatically specifying schema 
   ```
      from pyspark.sql.types import *
      
      data = [("johny","boy",32),("tom","Mckay",15)]
      
      fields = [StructField('fname', StringType(),True),StructField('lname', StringType(),True),StructField('Age', IntegerType(),True)] 
      
      schema = StructType(fields)
      
      newtable = hc.applySchema(data,schema)
      
      newtable.registerTempTable("poeple")
   ```   
      
      

   
   

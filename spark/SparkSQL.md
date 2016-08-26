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
  JSON files can be loaded using jsonFile() method of HiveContext/SQLContext
      
      `fpath = "file:///home/cloudera/Desktop/json_data/wbank1.json"
       jfile = hc.jsonFile(fpath)` 
      
  above json file can be loaded as temporary table which can be queries using SQL commands 
    
      `jfile.registerTempTable("table1")
       data = hc.sql("SELECT * FROM table1 WHERE board_approval_month = "November")
       data.show()`

###B. Loading paraquet files
Loading paraquet files is very much simialr to loading JSON files
    
    `jfile = hc.parquetFile(fpath)`

even paraquet file also can be loaded as temopary table using same `registerTempTable()` method

###C. Saving paraquet files 
incidently, data (i.e. DATAFRAME / SchemaRDD)  from SparkSQL can be saved as paraquet file using -

  ` data.saveAsParaquetFile("xyz.paraquet")`
  
##4. Working on rows  



  

   
   

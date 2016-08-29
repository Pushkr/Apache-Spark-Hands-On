#Avro Tools cheat sheet

- Avro tools is initialized using command "Avro-tools" on CLI.
- running just 'avro-tools' on cli, prints the list of available tools under avro-tools
- Most useful tools under avro-tools are `getschema`,`getmeta`, and `tojson` etc
- avro-tools <tool> gives additional information for passing arguments along for that tool
- Avro tools does not directly operate on HDFS files. 
For e.g. to get schema of a tables stored in mysql database, I had to first import tables using SQOOP to HDFS as -

```
sqoop import-all-tables \
--connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
--m 1 \
--username=retail_dba \
--password=cloudera \
--warehouse-dir= /user/hive/warehouse/retail_avro \
--as-avrodatafile
```

then using `HADOOP FS -get` command, downloaded avro file localy 

`hadoop fs -get /user/hive/warehouse/retail_avro/orders/part* ~/Desktop/avro`

In next step, avro tool is run using getmeta command as -

`avro-tools getmeta ~/Desktop/avro/part-m-00000.avro` 

this will simpley output avro data on console. Output of meta is not easy to read. `getschema` has pretty output.

`avro-tools getschema ~/Desktop/avro/part-m-00000.avro` 

Output from getmeta or getschema can be saved in file using unix's ">" operator as -

`avro-tools getschema ~/Desktop/avro/part-m-00000.avro > ~/Desktop/avro/schema.txt`


### from JSON to Binary (avro) 

`avro-tools fromjson tweet.json --schema-file tweeter.avsc > tweeter.avro`


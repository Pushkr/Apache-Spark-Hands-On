First create a external table and set avro.schema.url property pointing to current schema.

```

CREATE EXTERNAL TABLE TRAINS 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
STORED AS  AVRO
LOCATION  '/user/cloudera/avrotrain'
TBLPROPERTIES ('avro.schema.url' = 'hdfs:///user/cloudera/avrotrain/train_old.avsc');
```

Then load table using avro data 

```
LOAD DATA local INFILE '/home/cloudera/Desktop/data/part-m-00000.avro' into table TRAINS
```

check if data is OK

```
select * from trains limit 10;
```
check table properties to make sure schema url is correctly set
```
DESCRIBE FORMATTED TRAINS;
```

update schema file locally and upload to HDFS by overwriting old one.

```
hadoop fs -put -f  train.avsc /user/cloudera/avrotrain/train_old.avsc
```

reverify table using `DESCRIBE FORMATTED` 

When changing schema, if the column is added to the schema which is not present in existing table, use type of `['null','data-type'] `
and **must specify default value** 


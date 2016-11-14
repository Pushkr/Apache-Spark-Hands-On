- CREATING A MANAGED TABLE
```
	CREATE TABLE IF NOT EXISTS EMPLOYEES ( 
	EMP_NO INT,
	FIRST_NAME STRING,
	LAST_NAME STRING,
	HIRE_DATE STRING
	)
```
  ***"IF NOT EXISTS" CLAUSE WILL SUPRESS ERROR MESSAGE IF TABLE ALREADY EXISTS***
  
-----------------------------------------
 
- CREATING MANAGED TABLE WITH SPECIFIC FIELD AND ROWS FORMATS
```
	CREATE TABLE IF NOT EXISTS DEPT (
	DEPT_ID STRING,
	DEPT_NAME STRING,
	DEPT_MANAGER_ID INT,
	NO_OF_EMPLOYEES BIGINT
	)
	ROW FORMAT DELIMITED
	FIELDS TERMINATED BY '\001'
	LINES TERMINATED BY '\n';
```
-----------------------------------------

- CREATING EXTERNAL TABLE

```
	CREATE EXTERNAL TABLE IF NOT EXISTS EMP_EXT (
	EMP_NO INT,
	BIRTH_DATE STRING,
	FIRST_NAME STRING,
	LAST_NAME STRING,
	GENDER VARCHAR(1),
	HIRE_DATE STRING
	)
	ROW FORMAT DELIMITED
	FIELDS TERMINATED BY ',' 
	LINES TERMINATED BY '\n'
	LOCATION '/user/cloudera/employees.db/employees'
```

***NOTE***: WITHOUT ROW FORMAT SPECIFICATION ABOVE WILL NOT CORRECTLY READ EXTERNAL DATA

-----------------------------------------
- CREATE TABLE WITH PARQUET SERDE

```
	CREATE TABLE EMP_PARQ (
	EMP_NO INT,
	BIRTH_DATE STRING,
	FIRST_NAME STRING,
	LAST_NAME STRING,
	GENDER STRING,
	HIRE_DATE STRING)
	STORED AS PARQUET; 
```

-----------------------------------------

- CREATE TABLE WITH AVRO FILE FORMAt 

```
	CREATE TABLE orders_avro 
	ROW FORMAT SERDE
	  'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
	  STORED AS INPUTFORMAT
	  'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
	  OUTPUTFORMAT
	  'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
	  TBLPROPERTIES ('avro.schema.url' = 'hdfs://quickstart.cloudera:8020/user/cloudera/orders.avsc');
```

-----------------------------------------

- CREATE TABLE WITH JSON SERDE

In some distributions, a reference to hive-hcatalog-core.jar is required.

	ADD JAR '/usr/lib/hive-hcatalog/share/hcatalog/hive-hcatalog-core.jar';

create table using below -

	CREATE TABLE JSON_TABLE (product_id int,
	product_cat_id int,
	product_name string,
	product_description string,
	product_price double,
	product_image string)
	ROW FORMAT SERDE
	'org.apache.hive.hcatalog.data.JsonSerDe' 
	STORED AS TEXTFILE;

	ALTER TABLE JSON_TABLE SET LOCATION '/user/clooudera/json_table/sample.json'

-----------------------------------------

- Creating bucketed table

```
  CREATE TABLE IF NOT EXISTS JSON_TEMP (PRODUCT_ID INT,PRODUCT_NAME STRING)
  PARTITIONED BY (PRODUCT_PRICE_RANGE STRING)
  CLUSTERED BY (PRODUCT_ID) INTO 10 BUCKETS
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY '\t'
  LINES TERMINATED BY '\n';

  INSERT OVERWRITE TABLE JSON_TEMP PARTITION(PRODUCT_PRICE_RANGE)
  SELECT PRODUCT_ID,PRODUCT_NAME,'UNDER $50' AS PRODUCT_PRICE_RANGE
  FROM JSON_TABLE 
  WHERE PRODUCT_PRICE <= 50.00;
```

-----------------------------------------		


- CREATE PARTITIONED TABLE :
```
  CREATE TABLE IF NOT EXISTS EMP_PARTITIONED (
  EMP_NO INT,
  BIRTH_YEAR STRING,
  FIRST_NAME STRING,
  LAST_NAME STRING,
  HIRE_DATE STRING)
  PARTITIONED BY (HIRE_YEAR INT)
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY '\t'
  LINES TERMINATED BY '\n';
```
create a static partition :
	ALTER TABLE EMP_PARTITIONED ADD PARTITIONED (HIRE_YEAR = 2016)

inserting into partition

	INSERT INTO TABLE EMP_PARTITIONED PARTITION (HIRE_YEAR = 2016)
	VALUES (10001,'1984','HELENA','BARBA','2016-01-01');

CREATING DYNAMIC PARTITION;

	set hive.exec.dynamic.partition.mode = nonstrict;
	set hive.exec.max.dynamic.partitions = 2000;
	set hive.exec.max.dynamic.partitions.pernode = 2000;

	INSERT OVERWRITE TABLE EMP_PARTITIONED 
	PARTITION (HIRE_YEAR)
	SELECT EMP_NO, SUBSTR(BIRTH_DATE,1,4) AS BIRTH_YEAR,FIRST_NAME,LAST_NAME,
	HIRE_DATE,SUBSTR(HIRE_DATE,1,4) AS HIRE_YEAR 
	FROM DEFAULT.EMPLOYEES;
	
-----------------------------------------

- INSERTING DATA IN TABLE
	
	SINGLE INSERT :
		
    `INSERT INTO TABLE EMPLOYEES VALUES (10000,'1984-06-19','PUSHKAR','GUJAR','M','2008-06-27')`
	
		NOTE: THERE IS NO PRIMARY KEY CONCEPT IN HIVE. EXECUTING ABOVE COMMAND TWICE WILL NOT THROW ERROR
		EVEN IF EXACT SAME RECORD EXISTS

	INSERTING DATA FROM LOCAL FILE

		`LOAD DATA LOCAL INPATH 'file:///home/cloudera/desktop/localdata.txt' INTO TABLE EMPLOYEES`

	----------------------------------	
  INSERTING DATA IN TO PARQUET TABLE
  
  ```
		insert into table emp_parq 
		values(10000,'1984-06-19','pushkar','gujar','m','2016-09-18')
   ```
	INSERTING FROM ANOTHER TABLE USING QUERY

		`INSERT INTO TABLE EMP_PARQ SELECT * FROM DEFAULT.EMPLOYEES LIMIT 100;`

-----------------------------------------

- SIMPLE SELECT QUERY ON TABLE

in HIVE shell :

	SELECT * FROM EMPLOYEES WHERE EMP_NO=10000;

using hive CLI:

	`hive -e "select * from employees where emp_no=10000" --database solution3`

-----------------------------------------

- Additional commands 

	to find specific configuration properties using SET command -

	`hive -S -e "set" |grep warehouse`

	above command will print all the configuration properties on console that have word 'warehouse' in them


	to see currently working database

	`set hive.cli.print.current.db=true`

	command to see all the processes that are running on specific port
	
	`netstat -an|grep 3306`
	



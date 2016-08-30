# Hive Cheatsheet

- all commands must end with semi-colon to execute.

- To create a database or schema use `CREATE DATABASE/SCHEMA [IF NOT EXISTS] <NAME>` where `IF NOT EXISTS` is optional clause
  which when specified, does not throw error when the db/schema already exists.
  ```
  CREATE (DATABASE|SCHEMA) [IF NOT EXISTS] database_name
  [COMMENT database_comment]
  [LOCATION hdfs_path]
  [WITH DBPROPERTIES (property_name=property_value, ...)];
  ```
  
- Use `SHOW DATABASE` and `USE <DATABASE-NAME> ` to display list of databases and use particular database.

- Use `DROP DATABASE [IF EXISTS] <NAME>` to delete database. If there is table exists within database , DROP DATABASE will fail
  To delete database along with tables in it, use `DROP DATABASE [IF EXISTS] <NAME> CASCADE`

- Usual unix terminal commands can be executed by preceeding command with "!" (exclaimatory mark). for e.g.
  use `!clear` to clear screen.
 
- ## CREATE TABLE statement :
  ```
  CREATE[TEMPORARY][EXTERNAL] TABLE [IF NOT EXISTS] [db_name.] table-name
  (col_name data_type [COMMENT col_comment], ...)]
  [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]
  [ROW FORMAT row_format] 
  [STORED AS file_format]
  [LOCATION hdfs_path]
  [TBLPROPERTIES (property_name=property_value, ...)] 
  [AS select_statement];
  
  CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.]table_name
  LIKE existing_table_or_view_name
  [LOCATION hdfs_path];

  ```
where 
```
  row_format
    : DELIMITED [FIELDS TERMINATED BY char [ESCAPED BY char]] [COLLECTION ITEMS TERMINATED BY char]
          [MAP KEYS TERMINATED BY char] [LINES TERMINATED BY char]
          [NULL DEFINED AS char]   -- (Note: Available in Hive 0.13 and later)
    | SERDE serde_name [WITH SERDEPROPERTIES (property_name=property_value, property_name=property_value, ...)]
   
  file_format:
    : SEQUENCEFILE
    | TEXTFILE    -- (Default, depending on hive.default.fileformat configuration)
    | RCFILE      -- (Note: Available in Hive 0.6.0 and later)
    | ORC         -- (Note: Available in Hive 0.11.0 and later)
    | PARQUET     -- (Note: Available in Hive 0.13.0 and later)
    | AVRO        -- (Note: Available in Hive 0.14.0 and later)
    | INPUTFORMAT input_format_classname OUTPUTFORMAT output_format_classname
```

- ###Hive datatypes are : 
  - TINYINT
  - SMALLINT
  - INT
  - BIGINT
  - VARCHAR - upto 65k charachers
  - CHAR - uto 255 char
  - FLOAT
  - DOUBLE
  - DECIMAL(precision, scale)
  - DATE
  - TIMESTAMP
  - UNION - collection of heterogenous data
  - NULL
  - STRUCT - 
  - ARRAY 
  - MAP
  
  


  

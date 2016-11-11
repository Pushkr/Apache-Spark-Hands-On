

sqoop list-databases \
  --connect "jdbc:mysql://quickstart.cloudera:3306" \
  --username retail_dba \
  --password cloudera

sqoop list-tables \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera

sqoop eval \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --query "select count(1) from order_items"

sqoop import-all-tables \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --warehouse-dir=/user/cloudera/sqoop_import
  
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --table departments \
  --target-dir /user/cloudera/sqoop_import/retail.db/departments

#If we want to change the character that seperates fields and the one seperating lines :
  --fields-terminated-by '|' \
  --lines-terminated-by '\n' \

# Import query result
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --query="select * from orders join order_items on orders.order_id = order_items.order_item_order_id where \$CONDITIONS" \
  --target-dir /user/cloudera/sqoop_import/retail.db/order_join \
  --split-by order_id \ # We must specify the column with the index (Primary, foreign)
  --num-mappers 4

# HIVE 
# In this example, we assume that the department hive table already exists and we want to overwrite it.
# Otherwise we could add --hive-create-table
# Sqoop stores data in a temporary directory called the staging table under the user's home directory : /user/cloudera
# before copying data into Hive table. cloudera => /user/cloudera/department should not exists.
# The temporary directory is removed after the job is done.

sqoop import-all-tables \
  --num-mappers 1 \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --hive-import \
  --hive-overwrite \
  --hive-database "sqoop_import_test" #You can choose the database tou want
  --compress \
  --compression-codec org.apache.hadoop.io.compress.SnappyCodec \
  --outdir java_files
  
sqoop import 
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" 
  --username retail_dba 
  --password cloudera 
  --table=departments 
  --hive-home=/user/hive/warehouse 
  --hive-import 
  --hive-overwrite 
  --create-hive-table 
  --hive-table=sqoop_import.departments
  --outdir java_files

# Getting delta (--where) :  if there are new records in mysql database that need to be stored in HDFS.
# --append option is used to avoid the failure (department folder already exists). 
# N+1 is the index of the first new record to be stored in HDFS.

sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --table departments \
  --target-dir /user/cloudera/sqoop_import/retail.db/departments \
  --append \
  --where "department_id > N" \ 
  --outdir java_files

#Export data

mysql>> use retail_db;
mysql>> create table departments_export as select * from departments where 1=2;

hadoop fs -cp /user/cloudera/sqoop_import/retail.db/departments /user/cloudera/sqoop_export

sqoop export --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --table departments \
  --export-dir /user/cloudera/sqoop_export/departments \
  --num-mappers 2 \
  --batch \
  --outdir java_files

#To update rows : --update-key {primary_key}
#To insert while updating : --update-mode allowinsert

sqoop job --create sqoop_job \
  -- import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --table departments \
  --target-dir /user/cloudera/sqoop_import/departments \
  --fields-terminated-by '|' \
  --lines-terminated-by '\n' \
  --outdir java_files

sqoop job --list

sqoop job --show sqoop_job

sqoop job --exec sqoop_job

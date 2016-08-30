# DATA INGEST Assignment - Import data from a MySQL database into HDFS using Sqoop

#importing from mysql database serially i.e. with map tasks = 1

sqoop import --connect jdbc:mysql://localhost/cricket --table -m 1

#This gives warning that import is being made from mysql and this could be faster using '--direct' option

#Also if primary key wasnt specified for table, process terminates with warning to specify '--split-by' option

sqoop import --connect jdbc:mysql://localhost/cricket --table master --split-by lahmanID

#Importing in 'new' target directory and using direct mode. Directory must not be already existing. 
# import will create a new one automatically
sqoop import --connect jdbc:mysql://localhost/cricket \
             --table master \
             --target-dir newdirectory \
             -- direct
          

#Change the delimiter of data during import using Sqoop
sqoop import --connect jdbc:mysql://localhost/cricket \
--query 'SELECT lahmanID,weight,height FROM master WHERE height <= 150 and height > 0 AND $CONDITIONS' \
--target-dir newdb2 \
--fields-terminated-by "\t" 

#in above import statement, when specifying QUERY option, inclusion of $CONDITIONS and specifying SPLIT-BY option is manadatory. 


#Change the file type of data during import using Sqoop
sqoop import --connect jdbc:mysql://localhost/cricket  \
--query 'SELECT lahmanID,weight,height FROM master WHERE height > 150 AND $CONDITIONS' \
--target-dir newdb3 \
--fields-terminated-by '\t' \
--split-by lahmanID \
--lines-terminated-by X \
--as-sequencefile 

#DEFAULT MYSQL PORT IS 3306
#import all tables from mysql to HDFS in avro format

sqoop import-all-tables \
--connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
--m 1 \
--warehouse-dir=/user/hive/warehouse/retail_avro \
--as-avrodatafile \
--username=retail_dba \
--password=cloudera;

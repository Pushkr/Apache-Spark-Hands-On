sqoop import \
--connect jdbc:mysql://localhost:3306/employees \
--username root \
--password cloudera \
--table employees  \
--fields-terminated-by '\t' \
--lines-terminated-by '\n' \
--hive-database employees \
--hive-import;

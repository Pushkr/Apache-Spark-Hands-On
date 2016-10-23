 sqoop import-all-tables \
 --connect jdbc:mysql://localhost:3306/employees \
 --username root \
 --password cloudera \
 --hive-import \
 --fields-terminated-by ',' \
 --lines-terminated-by '\n' ;

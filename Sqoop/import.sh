#importing from mysql database serially i.e. with map tasks = 1

sqoop import --connect jdbc:mysql://localhost/cricket --table -m 1

#This gives warning that import is being made from mysql and this could be faster using '--direct' option

#Also if primary key wasnt specified for table, process terminates with warning to specify '--split-by' option

sqoop import --connect jdbc:mysql://localhost/cricket --table master --split-by lahmanID

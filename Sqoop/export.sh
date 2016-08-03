
#export data from HDFS to under1502 table in mysql. data is deliminated by character '-' (dash) while importing in HDFS. 

sqoop export --connect jdbc:mysql://localhost/cricket 
            --export-dir newdb5 --table under1502  
            --direct 
            --input-fields-terminated-by '-'

#This query is import data sucessfuly but only imports first column. input-fields-terminated-by seems to have no effect. more to come..

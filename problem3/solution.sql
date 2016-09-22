create database movies;
use movies;


#1. create a u_data table
#2. see the field descriptions of u_data table
#3. load data into u_data table from a local text file
#4. show all the data in the newly created u_data table
#5. show the numbers of item reviewed by each user in the newly created u_data table
#6. show the numbers of users reviewed each item in the newly created u_data table


CREATE TABLE U_DATA ( USERID INT, ITEMID INT ,RATING INT,TSTAMP TIMESTAMP) 
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INPATH 'file:///home/cloudera/Desktop/ass1/udata.txt' INTO TABLE U_DATA;

DESCRIBE FORMATTED U_DATA;

SELECT * FROM U_DATA;

SELECT USERID,COUNT(ITEMID) FROM U_DATA
GROUP BY USERID
ORDER BY USERID;

SELECT ITEMID,COUNT(USERID) FROM U_DATA 
GROUP BY ITEMID 
ORDER BY ITEMID;

'''
7. create a u_user table
8. see the field descriptions of u_user table
9. load data into u_user table from a local text file
10. show all the data in the newly created user table
11. count the number of data in the u_user table
12. count the number of user in the u_user table genderwise
'''


CREATE TABLE USER ( USERID INT,AGE INT,GENDER char(1), OCCUPATION STRING,ZIP STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';


LOAD DATA LOCAL INPATH 'file:///home/cloudera/Desktop/ass1/USER.TXT' INTO TABLE USER;

SELECT * FROM USER;

SELECT COUNT(*) FROM USER;

SELECT GENDER,COUNT(GENDER) FROM USER GROUP BY GENDER;


#13. join u_data table and u_user tables based on userid and show the top 10 results

SELECT * FROM U_DATA,USER WHERE U_DATA.USERID = USER.USERID LIMIT 10;

# login in to Mysql as root
mysql -u root -p

# create a database
CREATE DATABASE cricket;

# grant all access to localhost on database cricket
GRANT ALL PRIVILEGES ON cricket.* TO ''@'localhost';

# optional - to use database
use cricket;

# or instead of command 'use' , log back in databse directly using database name 
mysql cricket


#optional - to show tables under database
show tables;

# login again as localhost 
mysql -u cloudera -p

# create master table as -
CREATE TABLE master (
                    lahmanID INT NOT NULL, playerID VARCHAR(20),managerID VARCHAR(20),
                    hofID VARCHAR(20),birthYear YEAR,birthMonth INT,
                    birthDay INT,birthCountry VARCHAR(20),
                    birthCity VARCHAR(30),deathYear YEAR,deathMonth INT,
                    deathDay INT,deathCountry VARCHAR(20),
                    deathState VARCHAR(2),deathCity VARCHAR(20),
                    nameFirst VARCHAR(20),nameLast VARCHAR(20),
                    nameNote VARCHAR(50),nameGiven VARCHAR(30),nameNick VARCHAR(20),
                    weight INT,height INT,bats VARCHAR(1),
                    throws VARCHAR(1),debut DATE,finalGame DATE,
                    college VARCHAR(50),lahman40ID VARCHAR(20),lahman45ID VARCHAR(20),
                    retroID VARCHAR(20),holtzID VARCHAR(20),bbrefID VARCHAR(20)
                    );


#made mistake above. Didnt define PRIMARY KEY. 

ALTER TABLE master ADD PRIMARY KEY(lahmanID);



#import master.csv from local file system in to mysql database
LOAD DATA LOCAL INFILE 'Master.csv' 
  INTO TABLE master 
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '"' 
  LINES TERMINATED BY '\n';







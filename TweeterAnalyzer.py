from pyspark import SparkContext,SparkConf 
from pyspark.sql import SQLContext,Row
import json
import os
# Create configuartion 
conf = SparkConf().setAppName("TweeterAnalyzer").setMaster("local")

# Create sparkContext object
sc = SparkContext(conf = conf)

# Create HiveContext for SQL processing

hc = SQLContext(sc)

# read JSon file 
data = hc.read.json("file:///home/cloudera/Desktop/tweet.json")

data.printSchema()

data.registerTempTable("tweets")


def tweetsbyuser(userID):
	query = "SELECT user,text from tweets WHERE user='"+userID+"'"
	print(query)
	ex01 = hc.sql(query)
	return ex01

def totaltweetsbyall():
	query = "SELECT user,count(id) as NumOfTweets from tweets GROUP BY user ORDER BY NumOfTweets DESC"
	print(query)
	ex02 = hc.sql(query)
	return ex02

# Find all the tweets by user 
result01 = tweetsbyuser("Cas")
result01.show()
#result01.map(lambda row : (row.user,str(row.text))).saveAsTextFile("file:///home/cloudera/Desktop/output/TweetsByUser")

# Find total nnumber of tweets by each user
result02 = totaltweetsbyall()
result02.map(lambda row : (row.user,row.NumOfTweets)).saveAsTextFile("file:///home/cloudera/Desktop/output/UserTweetCount1")

#Alternate solution to above
countMap = data.map(lambda x : x['user']).countByValue()
# countMap will be a dictionary

# To save countMap is proper output format, convert it to list first
ListA = []
for k,v in countMap.items():
	ListA = ListA.append((k,v))

# Sort list by total count in descending order and save as file
sc.parallelize(sorted(listA,key=lambda x:x[1],reverse=True)).saveAsTextFile("file:///home/cloudera/Desktop/output/UserTweetCount2")

#Find all mentions
men = data.flatMap(lambda x :x['text'].split(" ")) \
	.filter(lambda x: len(x.strip()) > 1) \
	.filter(lambda x : x[0] == '@') \
	.map(lambda x:x.replace('@','')) 

Allmentions = sorted(set(men.collect()))
sc.parallelize(Allmentions).saveAsTextFile("file:///home/cloudera/Desktop/output/AllMentions")

#Count how many times each person is mentioned

menCountDict =  data.flatMap(lambda x :x['text'].split(" ")) \
		.filter(lambda x: len(x.strip()) > 1) \
		.filter(lambda x : x[0] == '@') \
		.countByValue()

MentionCounts = sorted([(k,v) for k,v in menCountDict],key=lambda x:x[1],reverse=true)
sc.parallelize(MentionCounts).saveAsTextFile("file:///home/cloudera/Desktop/output/MentionCount")

print("Top 10 mentioned persons are : ")
for i in range(11):
	print(Mentioncounts[i][0].replace('@','')+ " was mentioned : " Mentioncounts[i][1] + " times")
 
	








print("end of program")


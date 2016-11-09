from pyspark import SparkContext,SparkConf
from pyspark.sql import HiveContext,SQLContext,Row
import json

conf = SparkConf().setAppName("Task")
sc = SparkContext(conf=conf)
hc = HiveContext(sc)

hc.sql("set spark.sql.shuffle.partitions=10")

artists = hc.jsonFile("artists_en.json")
movies = hc.jsonFile("movies_en.json")

movies.registerTempTable("movies")
artists.registerTempTable("artists")

# function to print data using foreach
def printx(x) : 
  print(x)


#Question 2 solution :
movies_clean = hc.sql("select id,title,year,director,genre,country,actors from movies")

#Question 3 solution :
mUs_movies = hc.sql("select year,title from movies") \
.map(lambda row : (row.year,row.title)).groupByKey() \
.mapValues(lambda data : [title for title in data])

# Question 4 solution :
mUs_directors = hc.sql("select director,title from movies") \
.map(lambda row:(row.director,row.title)) \
.groupByKey() \
.map(lambda row : ((row[0].first_name,row[0].last_name,row[0].id,row[0].year_of_birth),[title for title in row[1]]))

#Question 5 solution:

def mapper1(record):
	output = []
	for actor in record.actors:
		output.append((record.id,actor.id,actor.role))
	return (actor for actor in output)

mUs_actors = movies.flatMap(mapper1) #MovieId,ActorId,Role

# Question 6 solution :
actors1 = mUs_actors.map(lambda row : (row[1],(row[0],row[2])))
artists1 = artists.map(lambda row: (row.id,(row.first_name,row.last_name,row.year_of_birth)))
artistsRdd = actors1.join(artists1)

mUs_actors_temp = artistsRdd.map(lambda row : (row[1][0][0],row[0],row[1][0][1],row[1][1][0],row[1][1][1],row[1][1][2]) ).sortBy(lambda row : -int(row[0].split(":")[1]))

mUs_actors_full = mUs_actors_temp.keyBy(lambda row : row[0]).groupByKey().mapValues(lambda data : [row for row in data])

# Question 7 solution :
def mapper2(record):
	output=[]
	for actor in record.actors:
		if actor.id == record.director.id:
			output.append((record.id,record.title,actor.id,actor.role))
	return (actor for actor in output)
rdd1 = movies.flatMap(mapper2).keyBy(lambda row : row[2]) # movieId,title,actorId,role

# Question 8 solution :

mUS_artists_as_actors_directors = joinedRdd1.groupByKey().mapValues(lambda row : [x for x in row]).foreach(f)

#Question 9 solution:
def customFilter(record):
	if str(record.director.first_name)[:1] == str(record.director.last_name)[:1]:
		return record
 
udf1 = movies.map(customFilter) \
	.filter(lambda row : row is not None) \
	.map(lambda row : (row.title,row.director.first_name,row.director.last_name,row.director.id,row.director.year_of_birth))

# Question 13 solution:
LongestTitle = movies.filter(movies.summary != 'None' ).map(lambda row : (row.title,row.summary)).reduce(lambda x,y : x if len(x[1]) > len(y[1]) else y)


sc.stop()

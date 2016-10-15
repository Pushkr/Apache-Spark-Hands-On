# question # 1: copy movies_en.json and artists_en.json to HDFS

#Solution :

hadoop fs -mkdir movies
hadoop fs -copyFromLocal 'file:///home/cloudera/Desktop/DATA/files/movies_en.json' movies/movies_en.json
hadoop fs -copyFromLocal 'file:///home/cloudera/Desktop/DATA/files/artists_en.json' movies/artists_en.json
hadoop fs -ls movies


#Question 2 : load two files in two relations and check if schema's are loaded correctly

start pyspark

hc = HiveContext(sc)
movies = hc.read.json("movies/movies_en.json")
movies.persist()
movies.printSchema()

artists = hc.read.json("movies/artists_en.json")
artists.persist()
artists.printSchema()

'''
DataFrame[actors: array<struct<id:string,role:string>>, country: string, director: struct<first_name:string,id:string,last_name:string,year_of_birth:string>, genre: string, id: string, summary: string, title: string, year: bigint]
'''

hc.sql("use default")
movies.registerTempTable("movies")

'''
hc.sql("alter TABLE movies REPLACE COLUMNS (actors ARRAY<STRUCT<id:string,role:string>>, \
country STRING, \
director STRUCT<first_name:STRING,id:STRING,last_name:STRING,year_of_birth:STRING>, \
genre STRING, \
id STRING, \
title STRING, \
year BIGINT)")
'''

# Question 3 : remove summary of movies 
hc.sql("CREATE TABLE newmovies AS SELECT actors,country, \
director,genre, \
id, title, year from movies")

# Alternate solution using python function
import json

# define a function to select the only required json fields
def json_cleaner(record):
	clean_record = {'actors':record.actors,
	                'country':record.country,
			'director':record.director,
			'genre':record.genre,
                        'id':record.id,
			'title':record.title,
			'year':record.year
			}
	return json.dumps(clean_record)

cleaned_movies = movies.map(json_cleaner)
cleaned_movies.saveAsTextFile("cleaned_json")

#--------------------


# Question 4 : Create a relation named mUS_year that groups the titles of American movies by year.
t1 = movies.map(lambda x : (x.year,x.title)).groupByKey()
mUs_year = t1.mapValues(lambda x : [names for names in x]).collect()


#Question 5 Create a relation named mUS_director that groups the titles of American movies by director
t2 = movies.filter(movies.country == 'USA') \
.map(lambda x : ((str(x.director.id),str(x.director.first_name),str(x.director.last_name),str(x.director.year_of_birth)),x.title)) \
.groupByKey()

mUS_director = t2.mapValues(lambda x : [str(names) for names in x]).collect()


##Question 6 : Create a relation named mUS_actors that contains (movieId, actorId, role) tuples. Each
#movie will appear in as many tuples as there are actors listed for that movie. Again, we only want to take
#American movies into account

t4 = hc.sql("select id as movie,actor.id as actor,actor.role as role  \
	     from movies \
	     LATERAL VIEW EXPLODE(actors) atable  as actor \
	     WHERE country = 'USA'")
mUs_actors = t4.map(lambda row: (row['movie'],row['actor'],row['role']))

# Question 7 : Create a relation named mUS_actors_full that associates the identifier of each American movie
#to the full description of each of its actors.

a1 = artists.map(lambda row: (row.id,(row.first_name,row.last_name,row.year_of_birth)))
a2 = t4.map(lambda row : (row.actor,(row.movie,row.role)))
a3 = a1.join(a2)
mUS_actors_full = a3.map(lambda row:(row[1][1][0],row[0],row[1][1][1],str(row[1][0][0])+" "+str(row[1][0][1]),row[1][0][2]))









 

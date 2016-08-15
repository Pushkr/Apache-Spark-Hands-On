# create spark context if already not available for stand alone application
groupId = org.apache.spark
artifactId = spark_core_2.10
version = 1.6.0

from pyspark import SparkContext,SparkConf
conf = SparkConf().setAppName("My app").setMaster("local")
sc = SparkContext(conf = conf)

#=======================================================================
# load simple text file using spark
file1 = sc.textFile("file:///home/cloudera/Desktop/pigdata/test1.txt")

#load text file with partitions . Make sure partitions are at least equal to number of cores in cluster or local machine
file1 = sc.textFile(""file:///home/cloudera/Desktop/data/test1.txt",4)

#load entire directory of text files. its will be loaded as key-value pair RDD with file name as keys
# and values are contents of text file.

dirFile = sc.wholeTextFiles("user/cloudera/master/part*")

# Saving text file. Output will be saved as directory containing multiple files. 

ListA = sc.parallelize([x for x in range(1,101)])
ListA.saveAsTextFile("file:///home/cloudera/Desktop/outputfile")

#=======================================================================


#Loading JSON files:
#==================
'''
Loading json file can be accomplished using textFile() methond and using parsing meth ods 
like "json.loads" (for string like objects) or "json.load" (for file like object)
I think, json.load may not be useful since we are loading file using spark method textFile()
already, that gives us RDD with string like object. Need to research this more...
'''

file = sc.textFile("data.json")
records = file.map(lambda x : json.loads(x))


#Saving json output is reverse of loading. String like data can be parsed thru "json.dumps()"
# and saved at end via saveAsTextFile() method

records.map(lambda x : json_dumps(x))
 .saveAsTextFile("json_output")
 
 
#=======================================================================
# Loading CSV files
#==================

'''
CSV can be loaded using same method of reading as textFile() and pasring using python
library "csv". 
csv.reader() and csv.writer() are two basic methods that can be used for simple read and
write operation. Both of these methods only create object for reading file. Actual row wise
reading/writing does not start until 'for' loop is run.
'''

'''
***Although, book recommends textfile + parsing method, a better method is using databrick's CSV package.
start up python-spark shell using -
'''
pyspark --package com.databricks:spark-csv_2.11:1.0.3 --master yarn-client

# and then read the file using 
df = sqlContext.read.format("com.databricks.spark.csv")
      .option("header", "true")
      .load("file:///home/cloudera/Desktop/HH.csv")



 





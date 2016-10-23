from pyspark import SparkContext,SparkConf
from pyspark.sql import HiveContext

conf = SparkConf().setAppName("Solution3")
sc = SparkContext(conf=conf)


# TO-DO : READ DATA FROM HDFS
data = sc.textFile("hdfs:///user/hive/warehouse/employees")       

#TO-DO : CHANGE DATA FORMAT

changed = data.map(lambda row : row.replace(',','\t'))

#to-do : save data

changed.saveAsTextFile("hdfs:///user/cloudera/solution3")

sc.stop()

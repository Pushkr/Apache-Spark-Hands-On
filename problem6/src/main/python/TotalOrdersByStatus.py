from pyspark import SparkContext,SparkConf

if __name__ == '__main__':
	
	conf = SparkConf().setAppName("Order By Status")
	sc = SparkContext(conf=conf)

	#read files

	orderByStatus = sc.textFile("hdfs:///user/hive/warehouse/orders")\
			.filter(lambda row : row!= '')\
			.map(lambda row : row.split("\001")) \
			.map(lambda row: (row[3],1))\
			.reduceByKey(lambda x,y: x+y)

	orderByStatus.sortBy(lambda row : row[1],False).coalesce(1).saveAsTextFile("OrdersByStatus")


	

	sc.stop(

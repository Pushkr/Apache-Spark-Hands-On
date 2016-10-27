from pyspark import SparkContext,SparkConf

if __name__ == '__main__':
	
	conf = SparkConf().setAppName("Total orders by order status for each date/month")
	sc = SparkContext(conf=conf)

	#read files

	orderByStatus = sc.textFile("hdfs:///user/hive/warehouse/orders")\
			.filter(lambda row : row!= '')\
			.map(lambda row : row.split("\001")) \
			.map(lambda row: ((row[1],row[3]),1)) \
			.reduceByKey(lambda x,y : x + y)
	

	orderByStatus\
	.sortByKey()\
	.map(lambda row : ",".join([row[0][0],row[0][1],str(row[1])]))\
	.saveAsTextFile("OrdersByStatusPerDate")
	
	sc.stop(

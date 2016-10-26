from pyspark import SparkContext,SparkConf

if __name__ == '__main__':
	
	conf = SparkConf().setAppName("total sales per month")
	sc = SparkContext(conf=conf)

	#read files

	orderFile = sc.textFile("hdfs:///user/hive/warehouse/orders")\
			.filter(lambda row : row!= '')\
			.map(lambda row : row.split("\001")) \
			.filter(lambda row: row[3] != "SUSPECT FRAUD" and row[3] != 'CANCELLED')

	itemFile  = sc.textFile("hdfs:///user/hive/warehouse/order_items")\
			.filter(lambda row : row!= '')\
			.map(lambda row : row.split("\001"))
	
	orderKV = orderFile.map(lambda row:(int(row[0]),row[1][:8])) # orderId,OrderYear-Month
	itemKV  = itemFile.map(lambda row: (int(row[1]),float(row[4]))) #orderID, subtotal
	

	joinedRdd = orderKV.join(itemKV)
	outputRdd = joinedRdd.map(lambda row: row[1]).reduceByKey(lambda x,y: x+y)
	
	outputRdd.saveAsTextFile("Sales_per_month")
	
	sc.stop()

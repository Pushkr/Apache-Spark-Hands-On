from pyspark import SparkContext,SparkConf

if __name__ == '__main__':
	
	conf = SparkConf().setAppName("Average Sales per day")
	sc = SparkContext(conf=conf)

	#read files
	orderFile = sc.textFile("hdfs:///user/hive/warehouse/retaildb.db/orders")\
	.filter(lambda row : row!= '')\
	.map(lambda row : row.split(",")) \
	.filter(lambda row: row[3] != "SUSPECT FRAUD" and row[3] != 'CANCELLED')

	itemFile  = sc.textFile("hdfs:///user/hive/warehouse/retaildb.db/order_items")\
			.filter(lambda row : row!= '')\
			.map(lambda row : row.split(","))

	orderKV = orderFile.map(lambda row:(int(row[0]),row[1][:11])).repartition(4) # orderId,OrderDate
	itemKV  = itemFile.map(lambda row: (int(row[1]),float(row[4]))).reduceByKey(lambda x,y : x+y).repartition(4)  #orderID, totalPerOrder


	joinedRDD = orderKV.join(itemKV)
	dateRDD = joinedRDD.map(lambda row : row[1]) \
			.aggregateByKey( \
				(0.0,0),\
				(lambda x,y : (x[0]+y,x[1]+1)) ,\
				(lambda row1,row2 : (row1[0]+row2[0],row1[1]+row2[1])) \
			)	# date, totalPerDate,totalnumberOfOrders
	avgRDD = dateRDD.mapValues(lambda row: row[0]/row[1])
	
	avgRDD.saveAsTextFile("Avg_Sales_per_day")
	sc.stop()

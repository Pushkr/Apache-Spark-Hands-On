from pyspark import SparkContext,SparkConf

if __name__ == '__main__':
	
	conf = SparkConf().setAppName("Average Sales Per Month")
	sc = SparkContext(conf=conf)

	#read files

	orderFile = sc.textFile("hdfs:///user/hive/warehouse/orders")\
			.filter(lambda row : row!= '')\
			.map(lambda row : row.split("\001")) \
			.filter(lambda row: row[3] != "SUSPECT FRAUD" and row[3] != 'CANCELLED')

	itemFile  = sc.textFile("hdfs:///user/hive/warehouse/order_items")\
			.filter(lambda row : row!= '')\
			.map(lambda row : row.split("\001"))

	orderKV = orderFile.map(lambda row:(int(row[0]),row[1][:7])).repartition(4) # orderId,OrderYear-Month

	itemKV  = itemFile.map(lambda row: (int(row[1]),float(row[4]))).reduceByKey(lambda x,y : x +y).repartition(4) #orderID, subtotal
		
	joinedRDD = orderKV.join(itemKV) # (orderID, (year-month, total))

	joinedMap = joinedRDD.map(lambda row: row[1]) # disgard orderID

	avgRDD = joinedMap.aggregateByKey((0.0,0), \
		(lambda total,record : (total[0]+record,total[1]+1)),\
		(lambda row1,row2 : (row1[0]+row2[0],row1[1]+row2[1])))

	avgRDDMap = avgRDD.mapValues(lambda row : row[0]/row[1]).sortBy(lambda row:row[1],False)

	avgRDDMap.coalesce(1).saveAsTextFile("AvgSalesPerMonth")	
	
	sc.stop()

from pyspark import SparkContext,SparkConf

if __name__ == '__main__' :

	conf = SparkConf().setAppName("Total sales for each date")
	sc = SparkContext(conf=conf)
	
	ordersFile = sc.textFile("hdfs:///user/hive/warehouse/retaildb.db/orders")
	itemsFile = sc.textFile("hdfs:///user/hive/warehouse/retaildb.db/order_items")
	
	kv_orders = ordersFile.map(lambda row : row.split(",")) \
        .filter(lambda row: row[3] != 'SUSPECTED_FRAUD' and row[3] != 'CANCELLED') \
        .map(lambda row : (int(row[0]),row[1]))
	
	kv_items = itemsFile.map(lambda row : row.split(","))\
        .map(lambda row : (int(row[2]),float(row[4])))


	joined = kv_orders.join(kv_items) # (orderid,(date,subtotal))

	bydate = joined.map(lambda row : row[1]).reduceByKey(lambda x,y : x + y)

	bydate.saveAsTextFile("sales_by_date")
		
	sc.stop()

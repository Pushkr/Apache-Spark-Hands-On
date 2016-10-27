from pyspark import SparkContext,SparkConf

if __name__ == '__main__':
	
	conf = SparkConf().setAppName("Repeat Customers Per Month")
	sc = SparkContext(conf=conf)

	#read files

	# orderId,Month
	Orders = sc.textFile("hdfs:///user/hive/warehouse/orders")\
			.filter(lambda row : row!= '')\
			.map(lambda row : row.split("\001")) \
			.filter(lambda row: row[3] != "SUSPECT FRAUD" and row[3] != 'CANCELLED') \
			.map(lambda row : (int(row[0]),int(row[1][5:7])))\
			.repartition(4)			

	# orderId,productId,quantity 
	Items = sc.textFile("hdfs:///user/hive/warehouse/order_items")\
	        	.filter(lambda row : row!= '')\
			.map(lambda row : row.split("\001")) \
			.map(lambda row : (int(row[1]),(int(row[2]),int(row[3]))))\
			.repartition(4) 


	#(orderID (month,(productID,quatity)) ) 
	joinedRDD = Orders.join(Items)



	def f(x): print(x)

	# ( (month,product),quantity) 
	joinedMap = joinedRDD.map(lambda row : row[1]).map(lambda row : ((row[0],row[1][0]),row[1][1])).reduceByKey(lambda x ,y : x+y)
	#	joinedMap.foreach(f)

	# (month, [(product, totalSold),........] )
	monthData = joinedMap.map(lambda row : (row[0][0],(row[0][1],row[1]))).groupByKey()
	

	def findtopthree(record):
		ListA = sorted(record[1],key=lambda data : data[1],reverse=True) # product and total sold list
		output = ListA[:3]
		data = [] 
		for item in output:
			data.append((record[0],item))
			
		
		return (y for y in data)
				
	outputRDD = monthData.flatMap(lambda row : findtopthree(row)).map(lambda row : ",".join([str(row[0]),str(row[1][0])]))
		
	outputRDD.saveAsTextFile("Top3ProductsPerMonth")

	sc.stop()

from pyspark import SparkContext,SparkConf
from pyspark.sql import HiveContext,Row

if __name__ == '__main__':
	
	conf = SparkConf().setAppName("Average Sales per day")
	sc = SparkContext(conf=conf)
	hc = HiveContext(sc)


	hc.sql("set spark.sql.shuffle.partitions = 10")

	orderMap = sc.textFile("hdfs:///user/hive/warehouse/retaildb.db/orders")\
	.map(lambda record : record.split(","))\
	.map(lambda record : Row(orderID=int(record[0]),orderDate=record[1][:11]))
	
	itemMap  = sc.textFile("hdfs:///user/hive/warehouse/retaildb.db/order_items")\
 	.map(lambda record : record.split(","))\
	.map(lambda row: (int(row[1]),float(row[4]))).reduceByKey(lambda x,y : x+y)\
	.map(lambda record : Row(orderID=int(record[0]),Total=record[1]))

	oSchema = hc.inferSchema(orderMap)
	iSchema = hc.inferSchema(itemMap)

	oSchema.registerTempTable("orders")
	iSchema.registerTempTable("items")

	avgSalesPerDay = hc.sql(" SELECT o.orderDate,avg(i.Total) as avgSales \
                            from orders o join items i \ 
                            where o.orderID = i.orderID \
                            group by o.orderDate \
                            order by avgSales DESC")


	avgSalesPerDay.map(lambda row : ",".join([row.orderDate,str(row.avgSales)]))\
  	.coalesce(1) \
  	.saveAsTextFile("AvgSalesPerDay2")

	sc.stop()

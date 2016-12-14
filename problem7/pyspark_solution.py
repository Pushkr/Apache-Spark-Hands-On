from pyspark import SparkContext,SparkConf
import random

rawFile = sc.textFile("/user/hive/warehouse/orders",1)

total = rawFile.count()
# order_id, order_date,customer_id,order_status 
rdd1 = rawFile.map(lambda row : row.split("\001"))

randomList = range(total)

random.shuffle(randomList)
randomRDD = sc.parallelize(randomList,1) 
orderid = rdd1.map(lambda row: row[0]).coalesce(1)
# random_numer,orderID
zip1 = randomRDD.zip(orderid)


random.shuffle(randomList)
randomRDD = sc.parallelize(randomList,1)
customerid = rdd1.map(lambda row : row[2]).coalesce(1)
# random_number,customer_ID
zip2 = randomRDD.zip(customerid)

final = zip1.join(zip2).map(lambda row : row[1]).saveAsTextFile('/user/cloudera/output')

sc.stop()

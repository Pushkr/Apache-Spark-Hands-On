import csv
import StringIO
from pyspark import SparkContext,SparkConf


conf = SparkConf().setAppName("Code1").setMaster("local[*]")
sc = SparkContext(conf= conf)
home = "file:///home/cloudera/Desktop/DATA/"
reit = "hdfs://quickstart.cloudera:8020/user/cloudera/user/hive/warehouse/reit"

# Method to load CSV file
def loader(line):
	input = StringIO.StringIO(line)
	reader = csv.DictReader(input,fieldnames=header_i)
	return reader.next()

# Method to write to CSV file
def writer(records):
	output = StringIO.StringIO(records)
	wrec = csv.DictWriter(output,fieldnames=header_o)
	for record in records:
		wrec.writerow(record)
	return [output.getvalue()] #returns contains of output file


header_i = ['orderID','dateTime','custID','status']
orders = sc.textFile(home+"orders.csv").map(loader)
closed = orders.map(lambda x : (x['status'],1)).reduceByKey(lambda x,y:x+y)



header_o = ['status','NoOforders']
data = closed.map(lambda x : {header_o[0]:x[0],header_o[1]:x[1]}) 
data.mapPartitions(writer).saveAsTextFile(home+"output1")

print("Current report of orders : \n")
for items in closed.collect():
	print(" %s are %d" %(str(items[0]),int(items[1])))

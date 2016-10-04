"""
  This script finds the statistics of month(s) in which top scoring 100 batsman were born.
"""
from pyspark import SparkContext,SparkConf
import calendar

conf = SparkConf().setAppName("BaseBall Stastistics").setMaster("local[*]")
sc = SparkContext(conf = conf)


#read files
mfile = sc.textFile("file:///home/cloudera/Desktop/baseball/master.csv")
bfile = sc.textFile("file:///home/cloudera/Desktop/baseball/batting.csv")

#persist files on cache
mfile.cache()
bfile.cache()

# remove empty lines,headers and parse as csv
map_split = mfile.filter(lambda x : len(x.strip())!=0).map(lambda x : x.split(",")).filter(lambda x : x[0] != 'lahmanID')  
bat_split = bfile.filter(lambda x : len(x.strip())!=0).map(lambda x : x.split(","))

#extract required key,value pair
kv_master = map_split.map(lambda x : (x[1],x[5])) # (playerID,BirthMonth)

kv_bat = bat_split.filter(lambda x : (x[0] != '' or x[8]!='')) \
.map(lambda x : (x[0],int(str(x[8]) if len(str(x[8]).strip())!=0 else 0))) \
.reduceByKey(lambda x,y : x+y) # (playerId, TotalRunsScored)

# Join 
joint = kv_master.join(kv_bat).map(lambda x : x[1]) # (playid,(month,TotalRunsScored))
d_joint = joint.distinct()
sorted_1 = d_joint.sortBy(lambda x : x[1],False)

'''
top_records= sorted_1.take(10) # get top 10 results

for record in top_records:
	temp = int(record[0])
	month = calendar.month_name[temp]
	print("player who scored %d was born in month of %s" % (record[1],month))
'''


top_months =  sorted(sc.parallelize(sorted_1.take(100))\
                       .map(lambda x : (x[0],1)) \
                       .reduceByKey(lambda x,y:x+y) \
                       .collect(),key=lambda x : x[1],reverse=True)

for m in top_months:
	temp = int(m[0])
	month = calendar.month_name[temp]
	print("%d out of 100 top scoring runners were born in month of %s" %(m[1],month))


sc.stop()

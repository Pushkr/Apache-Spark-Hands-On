 from pyspark import SparkContext,SparkConf
from pyspark.sql import HiveContext

conf = SparkConf().setAppName("Solution5")
sc = SparkContext(conf=conf)

sal1 = sc.textFile("hdfs:///user/hive/warehouse/salaries")
emp1 = sc.textFile("hdfs:///user/hive/warehouse/employees")

#get latest salaries from salary database
sal2 = sal1.map(lambda row : row.split(",")).map(lambda row: (int(row[0]),int(row[1]))).groupByKey()

def getMaxSalary(record):
	maxSal = max([x for x in record[1]])
	return (record[0],maxSal)

sal3 = sal2.map(getMaxSalary) 

 

emp2 = emp1.map(lambda row : row.split(",")).map(lambda row : (int(row[0]),row[4]))

female = emp2.filter(lambda row : row[1]=='F')
male = emp2.filter(lambda row : row[1] == 'M')


femSal = female.join(sal3) # (emp,(F,sal))
femSal1 = femSal.map(lambda row : (row[0],row[1][1]))

maleSal = male.join(sal3) # (emp,(F,sal))
maleSal1 = maleSal.map(lambda row : (row[0],row[1][1]))

Fsumsal = femSal1.map(lambda row : (row[1],1)).reduce(lambda acc,val : (acc[0] + val[0],acc[1] + val[1]))

Msumsal = maleSal1.map(lambda row : (row[1],1)).reduce(lambda acc,val : (acc[0] + val[0],acc[1] + val[1]))

b = float(Fsumsal[0]/Fsumsal[1])
c = float(Msumsal[0]/Msumsal[1])
print("Average female employee salary is : %f" %(b))
print("Average male employee salary is : %f" %(c))
sc.stop()

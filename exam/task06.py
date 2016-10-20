from pyspark import SparkConf,SparkContext

conf = SparkConf().setAppName("EmployeesWithLargestIncrement")
sc = SparkContext(conf=conf)

# read Data
step1 = sc.textFile("hdfs:///user/hive/warehouse/employees.db/salaries")
step1.cache()

# separate data
step2 = step1.map(lambda row : row.split(","))


# form a K-V pair of employeeID and Salary
step3 = step2.map(lambda row : (int(row[0]),int(row[1])))

# 
step4 = step3.groupByKey()

def findIncreament(record):
	minSalary = min(list(record[1]))
	maxSalary = max(list(record[1]))
	increament = (float(maxSalary - minSalary) / float(minSalary))  * 100
	return ( record[0],increament) 

def sortFunc(record):
	return record[1]

# 
step5 = step4.map(findIncreament).sortBy(sortFunc,False)

 
step5.coalesce(1).saveAsTextFile("hdfs:///user/cloudera/solution6")

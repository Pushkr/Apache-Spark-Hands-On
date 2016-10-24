import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.sql._


object task04{

	def main(args :Array[String]) {
	
	val sc = new SparkContext( new SparkConf().setAppName("task04"))
	val hc = new org.apache.spark.sql.hive.HiveContext(sc)

	hc.sql("set spark.sql.shuffle.partitions=10")

	hc.sql("use employees")

	
	val part1 = " join (select emp_no,title from titles where to_date = '9999-01-01') e"
	val part2 = " where e.emp_no = s.emp_no and s.salary > 75000 and s.salary <= 100000 and e.title='Senior Engineer'" 	

	val query = "select e.emp_no,e.title,s.salary from (select emp_no,salary from salaries where to_date = '9999-01-01') s" + part1 + part2
        
	val data = hc.sql(query)
	
	val output = data.map(row => row(0).toString + "," + row(1) +","+row(2).toString)

	output.saveAsTextFile("solution4")

	sc.stop()

	}

}

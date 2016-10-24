import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object task03 {

	def main(args:Array[String]){
	
	val sc = new SparkContext(new SparkConf().setAppName("task03"))
	
	val file = sc.textFile("hdfs:///user/hive/warehouse/employees.db/employees")
	
	val filemap = file.map( row => row.replaceAll(",","\t"))

	filemap.saveAsTextFile("solution3")

	sc.stop()
		

	}
}

package com.stock
import org.apache.spark.SparkContext._
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import _root_.com.stock.StockTick

object Stock {
def maxValuesReduce(a:StockTick,b:StockTick):StockTick ={
   /* TODO: Return a StockTick object with the maximum value between a and b for each one of its
      four fields (price, bid, ask, units)
   */
	var price = 0.0
        var ask = 0.0
        var bid = 0.0
        var units = 0	
	price = math.max(a.price,b.price)
	ask = math.max(a.ask,b.ask)
	bid = math.max(a.bid,b.bid)
	units = math.max(a.units,b.units)
        val NewTick = new StockTick(price=price,bid=bid,ask=ask,units=units)
	return NewTick
      }


def minValuesReduce(a:StockTick,b:StockTick): StockTick ={
   /* TODO: Return a StockTick object with the minimum value between a and b for each one of its
     four fields (price, bid, ask, units)
  */
	var price = 0.0
        var ask = 0.0
        var bid = 0.0
        var units = 0
	price = math.min(a.price,b.price)
	ask = math.min(a.ask,b.ask)
	bid = math.min(a.bid,b.bid)
	units = math.min(a.units,b.units)
	val NewTick = new StockTick(price=price,bid=bid,ask=ask,units=units)
	return NewTick
      }

def sumValuesReduce(a:StockTick,b:StockTick): StockTick ={
   /* TODO: Return a StockTick object with the addition of value of a and b for each one of its
     four fields (price, bid, ask, units)
  */
	var price = 0.0
        var ask = 0.0
        var bid = 0.0
        var units = 0
	price = a.price + b.price 
	ask = a.ask + b.ask
	bid = a.bid + b.bid 
	units = a.units + b.units 
	val NewTick = new StockTick(price=price,bid=bid,ask=ask,units=units)
	return NewTick
      }


  def main(args : Array[String]) {
  val sc = new SparkContext(new SparkConf().setAppName("Stock Analyzer"))
  

  val rawTickData = sc.textFile("tickdata_big.txt").filter(x => (x.trim).length() > 0)
  val tickData =  rawTickData.map(x => new StockTick(x))
  val goodTicks = tickData.filter(x => x.price > 0 & x.bid > 0 & x.ask > 0 & x.units > 0)
  goodTicks.cache()
  val numTicks =  goodTicks.count()
  System.out.println("total number of good tickdata points are: " + numTicks)
  

   val sumValues = goodTicks.reduce(Stock.sumValuesReduce)
   
   /*
   print("*"*20)
   print(sumValues.price,sumValues.ask,sumValues.bid,sumValues.units)
   */ 
   
   val maxValuesReduce = goodTicks.reduce(Stock.maxValuesReduce)  
   val minValuesReduce = goodTicks.reduce(Stock.minValuesReduce)  
   
   /*
   print(maxValuesReduce.price,maxValuesReduce.ask,maxValuesReduce.bid,maxValuesReduce.units)
   print(minValuesReduce.price,minValuesReduce.ask,minValuesReduce.bid,minValuesReduce.units)
   */
   val avgUnits = sumValues.units / numTicks.toDouble
   val avgPrice = sumValues.price / numTicks.toDouble

  System.out.println("Average Units are : " + avgUnits)
  System.out.println("Average Price is : " + avgPrice)

  sc.stop()
  }



}


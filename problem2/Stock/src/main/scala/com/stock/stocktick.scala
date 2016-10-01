package com.stock

class StockTick (val text_line:String="", var date:String="", var time:String="", 
    var price:Double=0.0, var bid:Double=0.0, var ask:Double=0.0, var units:Int=0) extends java.io.Serializable
{
  var tokens : Array[String] = new Array[String](4)
  if (text_line.length() !=0) {
         tokens = text_line.split(",")
         date = tokens(0)
         time = tokens(1)

         try {
            price = tokens(2).toDouble
            bid = tokens(3).toDouble
            ask = tokens(4).toDouble
            units = tokens(5).toInt
         } catch {
           case ex : Exception => {
                 price=0.0
                 bid = 0.0
                 ask = 0.0
                 units = 0
           }
          }
  }
  else{
         date = date
         time = time
         price = price
         bid = bid
         ask = ask
         units = units
  }
}

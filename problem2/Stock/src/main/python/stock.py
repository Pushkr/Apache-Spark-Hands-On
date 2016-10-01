import sys
from stocktick import StockTick
from pyspark import SparkContext
import datetime,time


def maxValuesReduce(a, b):
   ### TODO: Return a StockTick object with the maximum value between a and b for each one of its
   ### four fields (price, bid, ask, units)
	price,ask,bid,units = 0,0,0,0	
	price = max(a.price,b.price)
	ask = max(a.ask,b,ask)
	bid = max(a.bid,b.bid)
	units = max(a.units,b.units)
	return StockTick(price=price,bid=bid,ask=ask,units=units)



def minValuesReduce(a, b):
   ### TODO: Return a StockTick object with the minimum value between a and b for each one of its
   ### four fields (price, bid, ask, units)
	price,ask,bid,units = 0,0,0,0
	price = min(a.price,b.price)
	ask = min(a.ask,b.ask)
	bid = min(a.bid,b.bid)
	units = min(a.units,b.units)
	return StockTick(price=price,bid=bid,ask=ask,units=units)


def generateSpreadsDailyKeys(tick):  ### TODO: Write Me (see below)
	date = tick.date  
	time = tick.time
	k_date = datetime.date(int(date[6:10]),int(date[:2]),int(date[3:5]) ).isoformat()
	v_time = datetime.time(int(time[:2]),int(time[3:5]),int(time[6:8])).isoformat()
	spread = (tick.ask - tick.bid)/ 2*(tick.ask+tick.bid)
	return ((k_date,v_time),spread)
	
def generateSpreadsMonthlyKeys(tick):  ### TODO: Write Me (see below)
	date = tick.date  
	time = tick.time
	k_month = datetime.date(int(date[6:10]),int(date[:2]),int(date[3:5])).month
	v_time = datetime.time(int(time[:2]),int(time[3:5]),int(time[6:8])).isoformat()
	spread = (tick.ask - tick.bid)/ 2*(tick.ask+tick.bid)
	return ((k_month,v_time),spread)

def generateSpreadsHourlyKeys(tick):  ### TODO: Write Me (see below)
	date = tick.date  
	time_1 = tick.time
	k_hour = time.strptime(str(time_1),"%H:%M:%S").tm_hour
	v_time = datetime.time(int(time_1[:2]),int(time_1[3:5]),int(time_1[6:8])).isoformat()
	spread = (tick.ask - tick.bid)/ 2*(tick.ask+tick.bid)
	return ((k_hour,v_time),spread)


def spreadsSumReduce(a, b):          ### TODO: Write Me (see below)
	return (a[0]+b[0],a[1]+b[1])

#def generateSpreadsHourlyKeys(tick): ### TODO: Write Me (see below)


if __name__ == "__main__":
   """
   Usage: stock
   """
   sc = SparkContext(appName="StockTick")

   # rawTickData is a Resilient Distributed Dataset (RDD)
   rawTickData = sc.textFile("tickdata_big.txt").filter(lambda x : len(x.strip()) > 0)
   
   tickData =  rawTickData.map(lambda x : StockTick(x))
   goodTicks = tickData.filter(lambda x : x.price > 0 and x.bid > 0 and x.ask > 0 and x.units > 0)
  	
	
   ### TODO: store goodTicks in the in-memory cache
   goodTicks.cache()

   numTicks =  goodTicks.count()
   #print("VALUE OF numticks is : %d" %(int(numTicks)))	
	
   def sum_func(a,b):
	price = a.price + b.price
	bid = a.bid + b.bid
	ask = a.ask + b.ask
	units = a.units + b.units
	return StockTick(price,bid,ask,units)
	
	
   sumValues = goodTicks.reduce(lambda a,b: StockTick(price=a.price+b.price,bid=a.bid+b.bid,ask=a.ask+b.ask,units=a.units+b.units))
   #print("*"*20)
   #print(sumValues.price,sumValues.ask,sumValues.bid,sumValues.units)
   maxValuesReduce = goodTicks.reduce(maxValuesReduce) ### TODO: write the maxValuesReduce function
   minValuesReduce = goodTicks.reduce(minValuesReduce) ### TODO: write the minValuesReduce function
   #print("*"*20)
   #print(maxValuesReduce.price,maxValuesReduce.ask,maxValuesReduce.bid,maxValuesReduce.units)
   #print(minValuesReduce.price,minValuesReduce.ask,minValuesReduce.bid,minValuesReduce.units)
   avgUnits = sumValues.units / float(numTicks)
   avgPrice = sumValues.price / float(numTicks)

   print ("Max units %i, avg units %f\n" % (maxValuesReduce.units, avgUnits))
   print ("Max price %f, min price %f, avg price %f\n"% (maxValuesReduce.price, minValuesReduce.price, avgPrice))


   # Here is how the daily spread is computed. For each data point, the spread can be calculated
   # using the following formula : (ask - bid) / 2 * (ask + bid)
   # 1) We have a MapReduce phase that uses the generateSpreadsDailyKeys() function as an argument
   #    to map(), and the spreadsSumReduce() function as an argument to reduce()
   #    - The keys will be a unique date in the ISO 8601 format (so that sorting dates
   #      alphabetically will sort them chronologically)
   #    - The values will be tuples that contain adequates values to (1) only take one value into
   #      account per second (which value is picked doesn't matter), (2) sum the spreads for the
   #      day, and (3) count the number of spread values that have been added.
   # 2) We have a Map phase that computes thee average spread using (b) and (c)
   # 3) A final Map phase formats the output by producing a string with the following format:
   #    "<key (date)>, <average_spread>"
   # 4) The output is written using .saveAsTextFile("WDC_daily")


   # Daily Spread
   avgDailySpreads_1 = goodTicks.map(generateSpreadsDailyKeys).groupByKey().mapValues(lambda x : [spread for spread in x][0]).map(lambda x : (x[0][0],(x[1],1))) \
   .reduceByKey(spreadsSumReduce)    

   avgDailySpreads_2 = avgDailySpreads_1.map(lambda x: (x[0],float(x[1][0]/x[1][1])))         # (2)
   avgDailySpreads_3 = avgDailySpreads_2.sortByKey(True,1)                                   # (3)
   avg = avgDailySpreads_3.saveAsTextFile("WDC_Daily")                                        # (4)

 
   # For the monthly spread you only need to change the key. How?

   avgMonthlySpreads_1 = goodTicks.map(generateSpreadsMonthlyKeys).groupByKey().mapValues(lambda x : [spread for spread in x][0]).map(lambda x : (x[0][0],(x[1],1))) \
   .reduceByKey(spreadsSumReduce) 
			  
   avgMonthlySpreads_2 = avgMonthlySpreads_1.map(lambda x: (x[0],float(x[1][0]/x[1][1])))         # (2)
   avgMonthlySpreads_3 = avgMonthlySpreads_2.sortByKey(True,1)                                   # (3)
   avg = avgMonthlySpreads_3.saveAsTextFile("WDC_Monthly")                                        # (4)


   # Hourly
   avgHourlySpreads_1 = goodTicks.map(generateSpreadsHourlyKeys).groupByKey().mapValues(lambda x : [spread for spread in x][0]).map(lambda x : (x[0][0],(x[1],1))) \
   .reduceByKey(spreadsSumReduce) 
			  
   avgHourlySpreads_2 = avgHourlySpreads_1.map(lambda x: (x[0],float(x[1][0]/x[1][1])))         # (2)
   avgHourlySpreads_3 = avgHourlySpreads_2.sortByKey(True,1)                                   # (3)
   avg = avgHourlySpreads_3.saveAsTextFile("WDC_Hourly_2")                                        # (4)


   sc.stop()



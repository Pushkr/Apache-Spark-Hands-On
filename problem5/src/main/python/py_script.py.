
f1 = sc.textFile("flightdelays/fldata1.csv")
f2 = sc.textFile("flightdelays/fldata2.csv")
f3 = sc.textFile("flightdelays/fldata3.csv")

header = f1.first()

f1m = f1.filter(lambda x : (x != '' and x!=header)) \
.map(lambda x : x.split(",")) \
.filter(lambda x : x[4] != 'NA') \
.map(lambda x : ""+x[0]+","+x[1]+","+x[2]+","+x[4]+","+x[8]+","+x[9]+","+x[14]+","+x[16]+","+x[17]+"") 

f1m.saveAsTextFile("flightdelays_clean/fldata1.csv")

'''
Year, Month, DayofMonth, DepTime, UniqueCarrier, FlightNum, ArrDelay, Origin and Dest
'''

f2m = f2.filter(lambda x : (x != '' and x!=header)) \
.map(lambda x : x.split(",")) \
.filter(lambda x : x[4] != 'NA') \
.map(lambda x : ""+x[0]+","+x[1]+","+x[2]+","+x[4]+","+x[8]+","+x[9]+","+x[14]+","+x[16]+","+x[17]+"") 

f2m.saveAsTextFile("flightdelays_clean/fldata2.csv")
 


f3m = f3.filter(lambda x : (x != '' and x!=header)) \
.map(lambda x : x.split(",")) \
.filter(lambda x : x[4] != 'NA') \
.map(lambda x : ""+x[0]+","+x[1]+","+x[2]+","+x[4]+","+x[8]+","+x[9]+","+x[14]+","+x[16]+","+x[17]+"") 

f3m.saveAsTextFile("flightdelays_clean/fldata3.csv")

f1_cnt = f1m.count()
f2_cnt = f2m.count()
f3_cnt = f3m.count()

totalRows = f1_cnt + f2_cnt + f3_cnt

den1 = f1m.map(lambda x : x.split(",")).filter( lambda x : x[8] == "DEN").map(lambda x : ",".join(x))
den2 = f2m.map(lambda x : x.split(",")).filter( lambda x : x[8] == "DEN").map(lambda x : ",".join(x))
den3 = f1m.map(lambda x : x.split(",")).filter( lambda x : x[8] == "DEN").map(lambda x : ",".join(x))
den = (den1.union(den2)).union(den3)
den.coalesce(1).saveAsTextFile("denver_total")

den_60 = den.map(lambda x : x.split(",")) \
.filter(lambda x : (x[6] != '' and x[6] != 'NA')) \
.filter(lambda x : (float(x[6]) > 59)) \
.map(lambda x : ",".join(x))

den_60.coalesce(1).saveAsTextFile("denver_late")
 


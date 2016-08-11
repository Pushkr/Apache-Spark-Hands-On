RDD ==>
panda,0
pink,3
pirate,3
panda,1
pink,4

operation ==>

rdd.mapValues(lambda x:(x,1)).reduceBykeys(lambda x,y:(x[0]+y[0],x[1]+y[1]))

output:
panda, (1,2)
pink,(7,2)
pirate,(3,1)

explaination :
mapValues(lambda x:(x,1)) outputs a new rdd as -
{(panda,(0,1)),
  (pink,(3,1)),
  (pirate,(3,1)),
  (panda,(1,1)),
  (pink,(4,1))
}

reduceBykeys(lambda x,y:(x[0]+y[0],x[1]+y[1])) cummulatively adds values together for same keys as -
panda, ((0+1),(1+1))
pink,((3+4),(1+1))
pirate,(3,1)




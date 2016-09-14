- for sink types = HDFS,By default (when hdfs.fileType is not specified) ,flume will save files in SequenceFile format. 
- for avro files, use - 
``` 
agent.sinks.sink1.type = hdfs
agent.sinks.sink1.hdfs.fileType = DataStream
agent.sinks.sink1.serializer = avro_event
agent.sinks.sink1.serializer.compressionCodec = snappy

```

- **Partitioners** - event data gathered thru flume can be saved in partitioned format. Usually time format is used 

```
agent.sinks.sink1.hdfs.path = /tmp/flume/year=%Y/month=%m/day=%d
```

- **intercetors** - not all event data has timestamps. It can be added using interceptors.
  Flume has the capability to modify/drop events in-flight. 

```
agent.sources.source1.interceptors = int1
agent.sources.source1.interceptors.int1.type = timestamp
```


- **Fan out** - a single source can feed to multiple channels which in turn can feed to separate sinks.

```
agent1.sources  = s1
agent1.sinks = k1 k2
agent.channels = ch1 ch2

agent1.sources.s1.channels = ch1 ch2
agent1.sinks.k1.channel = ch1
agent1.sinks.k2.channel = ch2

agent1.channels.ch1.type = file
agent1.channels.ch2.type = memory

```

channel can be set optional by using `selector.optional` property on source

`agent1.sources.s1.selector.optional = ch2`

- **Sink Groups** - sink groups allows multiple sinks to be treated as one. To configure sinkgroup, agent's `sinkgroups` property 
is set to define group's name and then, `sinkgroups` lists `sinks` in group and `processor.type`

```
a1.sinkgroups = g1
a1.sinkgroups.g1.sinks = k1 k2
a1.sinkgroups.g1.processor.type = load_balance
```




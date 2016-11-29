
#### What is Hadoop Map Reduce ?

For processing large data sets in parallel across a hadoop cluster, Hadoop MapReduce framework is used.  Data analysis uses a two-step map and reduce process.

####  How Hadoop MapReduce works?

In MapReduce, during the map phase it counts the words in each document, while in the reduce phase it aggregates the data as per the document spanning the entire collection. During the map phase the input data is divided into splits for analysis by map tasks running in parallel across Hadoop framework.

#### Explain what is shuffling in MapReduce ?

The process by which the system performs the sort and transfers the map outputs to the reducer as inputs is known as the shuffle

#### Explain what is distributed Cache in MapReduce Framework ?

Distributed Cache is an important feature provided by map reduce framework. When you want to share some files across all nodes in Hadoop Cluster, DistributedCache  is used.  The files could be an executable jar files or simple properties file.

#### Explain what is NameNode in Hadoop?

NameNode in Hadoop is the node, where Hadoop stores all the file location information in HDFS (Hadoop Distributed File System).  In other words, NameNode is the centrepiece of an HDFS file system.  It keeps the record of all the files in the file system, and tracks the file data across the cluster or multiple machines

####  Explain what is JobTracker in Hadoop? What are the actions followed by Hadoop?

In Hadoop for submitting and tracking MapReduce jobs,  JobTracker is used. Job tracker run on its own JVM process

Hadoop performs following actions in Hadoop

Client application submit jobs to the job tracker
JobTracker communicates to the Namemode to determine data location
Near the data or with available slots JobTracker locates TaskTracker nodes
On chosen TaskTracker Nodes, it submits the work
When a task fails, Job tracker notify and decides what to do then.
The TaskTracker nodes are monitored by JobTracker

#### Explain what is heartbeat in HDFS?

Heartbeat is referred to a signal used between a data node and Name node, and between task tracker and job tracker, if the Name node or job tracker does not respond to the signal, then it is considered there is some issues with data node or task tracker

#### Explain what combiners is and when you should use a combiner in a MapReduce Job?

To increase the efficiency of MapReduce Program, Combiners are used.  The amount of data can be reduced with the help of combiner’s that need to be transferred across to the reducers. If the operation performed is commutative and associative you can use your reducer code as a combiner.  The execution of combiner is not guaranteed in Hadoop

####  What happens when a datanode fails ?

When a datanode fails

Jobtracker and namenode detect the failure
On the failed node all tasks are re-scheduled
Namenode replicates the users data to another node

#### Explain what is Speculative Execution?

In Hadoop during Speculative Execution a certain number of duplicate tasks are launched.  On different slave node, multiple copies of same map or reduce task can be executed using Speculative Execution. In simple words, if a particular drive is taking long time to complete a task, Hadoop will create a duplicate task on another disk.  Disk that finish the task first are retained and disks that do not finish first are killed.

#### Explain what are the basic parameters of a Mapper?

The basic parameters of a Mapper are

LongWritable and Text
Text and IntWritable

#### Explain what is the function of MapReducer partitioner?

The function of MapReducer partitioner is to make sure that all the value of a single key goes to the same reducer, eventually which helps evenly distribution of the map output over the reducers

#### Explain what is difference between an Input Split and HDFS Block?

Logical division of data is known as Split while physical division of data is known as HDFS Block

#### Explain what happens in textinformat ?

In textinputformat, each line in the text file is a record.  Value is the content of the line while Key is the byte offset of the line. For instance, Key: longWritable, Value: text

#### Mention what are the main configuration parameters that user need to specify to run Mapreduce Job ?

The user of Mapreduce framework needs to specify

Job’s input locations in the distributed file system
Job’s output location in the distributed file system
Input format
Output format
Class containing the map function
Class containing the reduce function
JAR file containing the mapper, reducer and driver classes

#### Explain what is WebDAV in Hadoop?

To support editing and updating files WebDAV is a set of extensions to HTTP.  On most operating system WebDAV shares can be mounted as filesystems , so it is possible to access HDFS as a standard filesystem by exposing HDFS over WebDAV.

#### Explain what is sqoop in Hadoop ?

To transfer the data between Relational database management (RDBMS) and Hadoop HDFS a tool is used known as Sqoop. Using Sqoop data can be transferred from RDMS like MySQL or Oracle into HDFS as well as exporting data from HDFS file to RDBMS

#### Explain how JobTracker schedules a task ?

The task tracker send out heartbeat messages to Jobtracker usually every few minutes to make sure that JobTracker is active and functioning.  The message also informs JobTracker about the number of available slots, so the JobTracker can stay upto date with where in the cluster work can be delegated

#### Explain what is Sequencefileinputformat?

Sequencefileinputformat is used for reading files in sequence. It is a specific compressed binary file format which is optimized for passing data between the output of one MapReduce job to the input of some other MapReduce job.

#### Explain what does the conf.setMapper Class do ?

Conf.setMapperclass  sets the mapper class and all the stuff related to map job such as reading data and generating a key-value pair out of the mapper

#### Explain what is Hadoop?

It is an open-source software framework for storing data and running applications on clusters of commodity hardware.  It provides enormous processing power and massive storage for any type of data.

#### Mention what is the difference between an RDBMS and Hadoop?

RDBMS	Hadoop
RDBMS is relational database management system	Hadoop is node based flat structure
It used for OLTP processing whereas Hadoop	It is currently used for analytical and for BIG DATA processing
In RDBMS, the database cluster uses the same data files stored in shared storage	In Hadoop, the storage data can be stored independently in each processing node.
You need to preprocess data before storing it	you don’t need to preprocess data before storing it

####  Mention Hadoop core components?

Hadoop core components include,

HDFS
MapReduce

#### What is NameNode in Hadoop?

NameNode in Hadoop is where Hadoop stores all the file location information in HDFS. It is the master node on which job tracker runs and consists of metadata.

#### Mention what are the data components used by Hadoop?

Data components used by Hadoop are

Pig
Hive

#### Mention what is the data storage component used by Hadoop?

The data storage component used by Hadoop is HBase.

####  Mention what are the most common input formats defined in Hadoop?

The most common input formats defined in Hadoop are;

TextInputFormat
KeyValueInputFormat
SequenceFileInputFormat

#### In Hadoop what is InputSplit?

It splits input files into chunks and assign each split to a mapper for processing.

#### For a Hadoop job, how will you write a custom partitioner?

You write a custom partitioner for a Hadoop job, you follow the following path

Create a new class that extends Partitioner Class
Override method getPartition
In the wrapper that runs the MapReduce
Add the custom partitioner to the job by using method set Partitioner Class or – add the custom partitioner to the job as a config file

#### For a job in Hadoop, is it possible to change the number of mappers to be created?

No, it is not possible to change the number of mappers to be created. The number of mappers is determined by the number of input splits.

#### Explain what is a sequence file in Hadoop?


To store binary key/value pairs, sequence file is used. Unlike regular compressed file, sequence file support splitting even when the data inside the file is compressed.

#### When Namenode is down what happens to job tracker?

Namenode is the single point of failure in HDFS so when Namenode is down your cluster will set off.

#### Explain how indexing in HDFS is done?

Hadoop has a unique way of indexing. Once the data is stored as per the block size, the HDFS will keep on storing the last part of the data which say where the next part of the data will be.

#### Explain is it possible to search for files using wildcards?

Yes, it is possible to search for files using wildcards.

#### List out Hadoop’s three configuration files?

The three configuration files are

core-site.xml
mapred-site.xml
hdfs-site.xml

#### Explain how can you check whether Namenode is working beside using the jps command?

Beside using the jps command, to check whether Namenode are working you can also use

/etc/init.d/hadoop-0.20-namenode status.

#### Explain what is “map” and what is "reducer" in Hadoop?

In Hadoop, a map is a phase in HDFS query solving.  A map reads data from an input location, and outputs a key value pair according to the input type.

In Hadoop, a reducer collects the output generated by the mapper, processes it, and creates a final output of its own.

#### In Hadoop, which file controls reporting in Hadoop?

In Hadoop, the hadoop-metrics.properties file controls reporting.

#### For using Hadoop list the network requirements?

For using Hadoop the list of network requirements are:

Password-less SSH connection
Secure Shell (SSH) for launching server processes

#### Mention what is rack awareness?

Rack awareness is the way in which the namenode determines on how to place blocks based on the rack definitions.

#### Explain what is a Task Tracker in Hadoop?

A Task Tracker in Hadoop is a slave node daemon in the cluster that accepts tasks from a JobTracker. It also sends out the heartbeat messages to the JobTracker, every few minutes, to confirm that the JobTracker is still alive.

#### Mention what daemons run on a master node and slave nodes?

Daemons run on Master node is "NameNode"
Daemons run on each Slave nodes are “Task Tracker” and "Data"

####  Explain how can you debug Hadoop code?

The popular methods for debugging Hadoop code are:

By using web interface provided by Hadoop framework
By using Counters

#### Explain what is storage and compute nodes?

The storage node is the machine or computer where your file system resides to store the processing data
The compute node is the computer or machine where your actual business logic will be executed.

####  Mention what is the use of Context Object?

The Context Object enables the mapper to interact with the rest of the Hadoop

system. It includes configuration data for the job, as well as interfaces which allow it to emit output.

####  Mention what is the next step after Mapper or MapTask?

The next step after Mapper or MapTask is that the output of the Mapper are sorted, and partitions will be created for the output.

#### Mention what is the number of default partitioner in Hadoop?

In Hadoop, the default partitioner is a “Hash” Partitioner.

#### Explain what is the purpose of RecordReader in Hadoop?

In Hadoop, the RecordReader loads the data from its source and converts it into (key, value) pairs suitable for reading by the Mapper.

####  Explain how is data partitioned before it is sent to the reducer if no custom partitioner is defined in Hadoop?

If no custom partitioner is defined in Hadoop, then a default partitioner computes a hash value for the key and assigns the partition based on the result.

#### Explain what happens when Hadoop spawned 50 tasks for a job and one of the task failed?

It will restart the task again on some other TaskTracker if the task fails more than the defined limit.

#### Mention what is the best way to copy files between HDFS clusters?

The best way to copy files between HDFS clusters is by using multiple nodes and the distcp command, so the workload is shared.

#### Mention what is the difference between HDFS and NAS?

HDFS data blocks are distributed across local drives of all machines in a cluster while NAS data is stored on dedicated hardware.

#### Mention how Hadoop is different from other data processing tools?

In Hadoop, you can increase or decrease the number of mappers without worrying about the volume of data to be processed.

####  Mention what job does the conf class do?

Job conf class separate different jobs running on the same cluster.  It does the job level settings such as declaring a job in a real environment.

####  Mention what is the Hadoop MapReduce APIs contract for a key and value class?

For a key and value class, there are two Hadoop MapReduce APIs contract

The value must be defining the org.apache.hadoop.io.Writable interface
The key must be defining the org.apache.hadoop.io.WritableComparable interface

#### Mention what are the three modes in which Hadoop can be run?

The three modes in which Hadoop can be run are

Pseudo distributed mode
Standalone (local) mode
Fully distributed mode

####  Mention what does the text input format do?

The text input format will create a line object that is an hexadecimal number.  The value is considered as a whole line text while the key is considered as a line object. The mapper will receive the value as ‘text’ parameter while key as ‘longwriteable’ parameter.

####  Mention how many InputSplits is made by a Hadoop Framework?

Hadoop will make 5 splits

1 split for 64K files
2 split for 65mb files
2 splits for 127mb files

####  Mention what is distributed cache in Hadoop?

Distributed cache in Hadoop is a facility provided by MapReduce framework.  At the time of execution of the job, it is used to cache file.  The Framework copies the necessary files to the slave node before the execution of any task at that node.

#### Explain how does Hadoop Classpath plays a vital role in stopping or starting in Hadoop daemons?

Classpath will consist of a list of directories containing jar files to stop or start daemons.



####  What is Big Data? 

Big data is defined as the voluminous amount of structured, unstructured or semi-structured data that has huge potential for mining but is so large that it cannot be processed using traditional database systems. Big data is characterized by its high velocity, volume and variety that requires cost effective and innovative methods for information processing to draw meaningful business insights. More than the volume of the data – it is the nature of the data that defines whether it is considered as Big Data or not.
 

####  What do the four V’s of Big Data denote? Click here to Tweet

IBM has a nice, simple explanation for the four critical features of big data:
a) Volume –Scale of data
b) Velocity –Analysis of streaming data
c) Variety – Different forms of data
d) Veracity –Uncertainty of data

#### How big data analysis helps businesses increase their revenue? Give example.Click here to Tweet

Big data analysis is helping businesses differentiate themselves – for example Walmart the world’s largest retailer in 2014 in terms of revenue - is using big data analytics to increase its sales through better predictive analytics, providing customized recommendations and launching new products based on customer preferences and needs. Walmart observed a significant 10% to 15% increase in online sales for $1 billion in incremental revenue. There are many more companies like Facebook, Twitter, LinkedIn, Pandora, JPMorgan Chase, Bank of America, etc. using big data analytics to boost their revenue.


####  Name some companies that use Hadoop. Click here to tweet this question

Yahoo (One of the biggest user & more than 80% code contributor to Hadoop)
Facebook
Netflix
Amazon
Adobe
eBay
Hulu
Spotify
Rubikloud
Twitter


####  Differentiate between Structured and Unstructured data.Click here to Tweet

Data which can be stored in traditional database systems in the form of rows and columns, for example the online purchase transactions can be referred to as Structured Data. Data which can be stored only partially in traditional database systems, for example, data in XML records can be referred to as semi structured data. Unorganized and raw data that cannot be categorized as semi structured or structured data is referred to as unstructured data. Facebook updates, Tweets on Twitter, Reviews, web logs, etc. are all examples of unstructured data.

####  On what concept the Hadoop framework works? Click here to Tweet

Hadoop Framework works on the following two core components-

- HDFS – Hadoop Distributed File System is the java based file system for scalable and reliable storage of large datasets. Data in HDFS is stored in the form of blocks and it operates on the Master Slave Architecture.

- Hadoop MapReduce-This is a java based programming paradigm of Hadoop framework that provides scalability across various Hadoop clusters. MapReduce distributes the workload into various tasks that can run in parallel. Hadoop jobs perform 2 separate tasks- job. The map job breaks down the data sets into key-value pairs or tuples. The reduce job then takes the output of the map job and combines the data tuples to into smaller set of tuples. The reduce job is always performed after the map job is executed.
 

####  What are the main components of a Hadoop Application? Click here to Tweet

Hadoop applications have wide range of technologies that provide great advantage in solving complex business problems.

Core components of a Hadoop application are-

1) Hadoop Common

2) HDFS

3) Hadoop MapReduce

4) YARN

Data Access Components are - Pig and Hive

Data Storage Component is - HBase

Data Integration Components are - Apache Flume, Sqoop, Chukwa

Data Management and Monitoring Components are - Ambari, Oozie and Zookeeper.

Data Serialization Components are - Thrift and Avro

Data Intelligence Components are - Apache Mahout and Drill.

####  What is Hadoop streaming? Click here to Tweet

Hadoop distribution has a generic application programming interface for writing Map and Reduce jobs in any desired programming language like Python, Perl, Ruby, etc. This is referred to as Hadoop Streaming. Users can create and run jobs with any kind of shell scripts or executable as the Mapper or Reducers.

####  What is the best hardware configuration to run Hadoop? Click here to Tweet

The best configuration for executing Hadoop jobs is dual core machines or dual processors with 4GB or 8GB RAM that use ECC memory. Hadoop highly benefits from using ECC memory though it is not low - end. ECC memory is recommended for running Hadoop because most of the Hadoop users have experienced various checksum errors by using non ECC memory. However, the hardware configuration also depends on the workflow requirements and can change accordingly.

####  What are the most commonly defined input formats in Hadoop? Click here to Tweet

The most common Input Formats defined in Hadoop are:

Text Input Format- This is the default input format defined in Hadoop.
Key Value Input Format- This input format is used for plain text files wherein the files are broken down into lines.
Sequence File Input Format- This input format is used for reading files in sequence.
We have further categorized Big Data Interview Questions for Freshers and Experienced-


####  What is a block and block scanner in HDFS? Click here to Tweet

Block - The minimum amount of data that can be read or written is generally referred to as a “block” in HDFS. The default size of a block in HDFS is 64MB.

Block Scanner - Block Scanner tracks the list of blocks present on a DataNode and verifies them to find any kind of checksum errors. Block Scanners use a throttling mechanism to reserve disk bandwidth on the datanode.

####  Explain the difference between NameNode, Backup Node and Checkpoint NameNode.  

NameNode: NameNode is at the heart of the HDFS file system which manages the metadata i.e. the data of the files is not stored on the NameNode but rather it has the directory tree of all the files present in the HDFS file system on a hadoop cluster. NameNode uses two files for the namespace-

fsimage file- It keeps track of the latest checkpoint of the namespace.

edits file-It is a log of changes that have been made to the namespace since checkpoint.

Checkpoint Node-

Checkpoint Node keeps track of the latest checkpoint in a directory that has same structure as that of NameNode’s directory. Checkpoint node creates checkpoints for the namespace at regular intervals by downloading the edits and fsimage file from the NameNode and merging it locally. The new image is then again updated back to the active NameNode.

BackupNode:

Backup Node also provides check pointing functionality like that of the checkpoint node but it also maintains its up-to-date in-memory copy of the file system namespace that is in sync with the active NameNode.

####  What is commodity hardware?  

Commodity Hardware refers to inexpensive systems that do not have high availability or high quality. Commodity Hardware consists of RAM because there are specific services that need to be executed on RAM. Hadoop can be run on any commodity hardware and does not require any super computer s or high end hardware configuration to execute jobs.

####  What is the port number for NameNode, Task Tracker and Job Tracker?  

NameNode 50070

Job Tracker 50030

Task Tracker 50060

#### Explain about the process of inter cluster data copying.  

HDFS provides a distributed data copying facility through the DistCP from source to destination. If this data copying is within the hadoop cluster then it is referred to as inter cluster data copying. DistCP requires both source and destination to have a compatible or same version of hadoop.

####  How can you overwrite the replication factors in HDFS?  

The replication factor in HDFS can be modified or overwritten in 2 ways-

1)Using the Hadoop FS Shell, replication factor can be changed per file basis using the below command-

$hadoop fs –setrep –w 2 /my/test_file (test_file is the filename whose replication factor will be set to 2)

2)Using the Hadoop FS Shell, replication factor of all files under a given directory can be modified using the below command-

3)$hadoop fs –setrep –w 5 /my/test_dir (test_dir is the name of the directory and all the files in this directory will have a replication factor set to 5)

Attend a Hadoop Interview session with experts from the industry!

####  Explain the difference between NAS and HDFS.  

NAS runs on a single machine and thus there is no probability of data redundancy whereas HDFS runs on a cluster of different machines thus there is data redundancy because of the replication protocol.
NAS stores data on a dedicated hardware whereas in HDFS all the data blocks are distributed across local drives of the machines.
In NAS data is stored independent of the computation and hence Hadoop MapReduce cannot be used for processing whereas HDFS works with Hadoop MapReduce as the computations in HDFS are moved to data.

####  Explain what happens if during the PUT operation, HDFS block is assigned a replication factor 1 instead of the default value 3. Click here to Tweet

Replication factor is a property of HDFS that can be set accordingly for the entire cluster to adjust the number of times the blocks are to be replicated to ensure high data availability. For every block that is stored in HDFS, the cluster will have n-1 duplicated blocks. So, if the replication factor during the PUT operation is set to 1 instead of the default value 3, then it will have a single copy of data. Under these circumstances when the replication factor is set to 1 ,if the DataNode crashes under any circumstances, then only single copy of the data would be lost.

####  What is the process to change the files at arbitrary locations in HDFS? Click here to Tweet

HDFS does not support modifications at arbitrary offsets in the file or multiple writers but files are written by a single writer in append only format i.e. writes to a file in HDFS are always made at the end of the file.

####  Explain about the indexing process in HDFS. Click here to Tweet

Indexing process in HDFS depends on the block size. HDFS stores the last part of the data that further points to the address where the next part of data chunk is stored.

####  What is a rack awareness and on what basis is data stored in a rack? Click here to Tweet

All the data nodes put together form a storage area i.e. the physical location of the data nodes is referred to as Rack in HDFS. The rack information i.e. the rack id of each data node is acquired by the NameNode. The process of selecting closer data nodes depending on the rack information is known as Rack Awareness.

The contents present in the file are divided into data block as soon as the client is ready to load the file into the hadoop cluster. After consulting with the NameNode, client allocates 3 data nodes for each data block. For each data block, there exists 2 copies in one rack and the third copy is present in another rack. This is generally referred to as the Replica Placement Policy.

####  What happens to a NameNode that has no data?

There does not exist any NameNode without data. If it is a NameNode then it should have some sort of data in it.

####  What happens when a user submits a Hadoop job when the NameNode is down- does the job get in to hold or does it fail.

The Hadoop job fails when the NameNode is down.

#### What happens when a user submits a Hadoop job when the Job Tracker is down- does the job get in to hold or does it fail.

The Hadoop job fails when the Job Tracker is down.

####  Whenever a client submits a hadoop job, who receives it?

NameNode receives the Hadoop job which then looks for the data requested by the client and provides the block information. JobTracker takes care of resource allocation of the hadoop job to ensure timely completion.


-------------------------------------------------------------
Hadoop MapReduce Interview Questions and Answers

####  Explain the usage of Context Object. Click here to Tweet

Context Object is used to help the mapper interact with other Hadoop systems. Context Object can be used for updating counters, to report the progress and to provide any application level status updates. ContextObject has the configuration details for the job and also interfaces, that helps it to generating the output.

####  What are the core methods of a Reducer? Click here to Tweet

The 3 core methods of a reducer are –

1)setup () – This method of the reducer is used for configuring various parameters like the input data size, distributed cache, heap size, etc.

Function Definition- public void setup (context)

#### reduce () it is heart of the reducer which is called once per key with the associated reduce task.

Function Definition -public void reduce (Key,Value,context)

#### cleanup () - This method is called only once at the end of reduce task for clearing all the temporary files.

Function Definition -public void cleanup (context)

#### Explain about the partitioning, shuffle and sort phase Click here to Tweet

Shuffle Phase-Once the first map tasks are completed, the nodes continue to perform several other map tasks and also exchange the intermediate outputs with the reducers as required. This process of moving the intermediate outputs of map tasks to the reducer is referred to as Shuffling.

Sort Phase- Hadoop MapReduce automatically sorts the set of intermediate keys on a single node before they are given as input to the reducer.

Partitioning Phase-The process that determines which intermediate keys and value will be received by each reducer instance is referred to as partitioning. The destination partition is same for any key irrespective of the mapper instance that generated it.

####  How to write a custom partitioner for a Hadoop MapReduce job? Click here to Tweet

Steps to write a Custom Partitioner for a Hadoop MapReduce Job-

A new class must be created that extends the pre-defined Partitioner Class.
getPartition method of the Partitioner class must be overridden.
The custom partitioner to the job can be added as a config file in the wrapper which runs Hadoop MapReduce or the custom partitioner can be added to the job by using the set method of the partitioner class.

------------------------------------------------------------------------
Hadoop HBase Interview Questions and Answers

####  When should you use HBase and what are the key components of HBase?

HBase should be used when the big data application has –

1)A variable schema

2)When data is stored in the form of collections

3)If the application demands key based access to data while retrieving.

Key components of HBase are –

Region- This component contains memory data store and Hfile.

Region Server-This monitors the Region.

HBase Master-It is responsible for monitoring the region server.

Zookeeper- It takes care of the coordination between the HBase Master component and the client.

Catalog Tables-The two important catalog tables are ROOT and META.ROOT table tracks where the META table is and META table stores all the regions in the system.

#### What are the different operational commands in HBase at record level and table level?

Record Level Operational Commands in HBase are –put, get, increment, scan and delete.

Table Level Operational Commands in HBase are-describe, list, drop, disable and scan.

####  What is Row Key?

Every row in an HBase table has a unique identifier known as RowKey. It is used for grouping cells logically and it ensures that all cells that have the same RowKeys are co-located on the same server. RowKey is internally regarded as a byte array.

####  Explain the difference between RDBMS data model and HBase data model.

RDBMS is a schema based database whereas HBase is schema less data model.

RDBMS does not have support for in-built partitioning whereas in HBase there is automated partitioning.

RDBMS stores normalized data whereas HBase stores de-normalized data.

####  Explain about the different catalog tables in HBase?

The two important catalog tables in HBase, are ROOT and META. ROOT table tracks where the META table is and META table stores all the regions in the system.

#### What is column families? What happens if you alter the block size of ColumnFamily on an already populated database?

The logical deviation of data is represented through a key known as column Family. Column families consist of the basic unit of physical storage on which compression features can be applied. In an already populated database, when the block size of column family is altered, the old data will remain within the old block size whereas the new data that comes in will take the new block size. When compaction takes place, the old data will take the new block size so that the existing data is read correctly.

####  Explain the difference between HBase and Hive.

HBase and Hive both are completely different hadoop based technologies-Hive is a data warehouse infrastructure on top of Hadoop whereas HBase is a NoSQL key value store that runs on top of Hadoop. Hive helps SQL savvy people to run MapReduce jobs whereas HBase supports 4 primary operations-put, get, scan and delete. HBase is ideal for real time querying of big data where Hive is an ideal choice for analytical querying of data collected over period of time.

####  Explain the process of row deletion in HBase.

On issuing a delete command in HBase through the HBase client, data is not actually deleted from the cells but rather the cells are made invisible by setting a tombstone marker. The deleted cells are removed at regular intervals during compaction.

####  What are the different types of tombstone markers in HBase for deletion?

There are 3 different types of tombstone markers in HBase for deletion-

1)Family Delete Marker- This markers marks all columns for a column family.

2)Version Delete Marker-This marker marks a single version of a column.

3)Column Delete Marker-This markers marks all the versions of a column.

####  Explain about HLog and WAL in HBase.

All edits in the HStore are stored in the HLog. Every region server has one HLog. HLog contains entries for edits of all regions performed by a particular Region Server.WAL abbreviates to Write Ahead Log (WAL) in which all the HLog edits are written immediately.WAL edits remain in the memory till the flush period in case of deferred log flush.

----------------------------------------------------------------

Hadoop Sqoop Interview Questions and Answers

####  Explain about some important Sqoop commands other than import and export.

`Create Job (--create)`

Here we are creating a job with the name my job, which can import the table data from RDBMS table to HDFS. The following command is used to create a job that is importing data from the employee table in the db database to the HDFS file.
```
$ Sqoop job --create myjob \
--import \
--connect jdbc:mysql://localhost/db \
--username root \
--table employee --m 1
```
Verify Job (--list)

‘--list’ argument is used to verify the saved jobs. The following command is used to verify the list of saved Sqoop jobs.

`$ Sqoop job --list`

Inspect Job (--show)

‘--show’ argument is used to inspect or verify particular jobs and their details. The following command and sample output is used to verify a job called myjob.

`$ Sqoop job --show myjob`

Execute Job (--exec)

‘--exec’ option is used to execute a saved job. The following command is used to execute a saved job called myjob.

`$ Sqoop job --exec myjob`

####  How Sqoop can be used in a Java program?

The Sqoop jar in classpath should be included in the java code. After this the method Sqoop.runTool () method must be invoked. The necessary parameters should be created to Sqoop programmatically just like for command line.

####  What is the process to perform an incremental data load in Sqoop?

The process to perform incremental data load in Sqoop is to synchronize the modified or updated data (often referred as delta data) from RDBMS to Hadoop. The delta data can be facilitated through the incremental load command in Sqoop.

Incremental load can be performed by using Sqoop import command or by loading the data into hive without overwriting it. The different attributes that need to be specified during incremental load in Sqoop are-

1)Mode (incremental) –The mode defines how Sqoop will determine what the new rows are. The mode can have value as Append or Last Modified.

2)Col (Check-column) –This attribute specifies the column that should be examined to find out the rows to be imported.

3)Value (last-value) –This denotes the maximum value of the check column from the previous import operation.

####  Is it possible to do an incremental import using Sqoop?

Yes, Sqoop supports two types of incremental imports-

1)Append

2)Last Modified

To insert only rows Append should be used in import command and for inserting the rows and also updating Last-Modified should be used in the import command.

####  What is the standard location or path for Hadoop Sqoop scripts?

/usr/bin/Hadoop Sqoop

####  How can you check all the tables present in a single database using Sqoop?

The command to check the list of all tables present in a single database using Sqoop is as follows-

Sqoop list-tables –connect jdbc: mysql: //localhost/user;

####  How are large objects handled in Sqoop?

Sqoop provides the capability to store large sized data into a single field based on the type of data. Sqoop supports the ability to store-

1)CLOB ‘s – Character Large Objects

2)BLOB’s –Binary Large Objects

Large objects in Sqoop are handled by importing the large objects into a file referred as “LobFile” i.e. Large Object File. The LobFile has the ability to store records of huge size, thus each record in the LobFile is a large object.

#### Can free form SQL queries be used with Sqoop import command? If yes, then how can they be used?

Sqoop allows us to use free form SQL queries with the import command. The import command should be used with the –e and – query options to execute free form SQL queries. When using the –e and –query options with the import command the –target dir value must be specified.

####  Differentiate between Sqoop and distCP.

DistCP utility can be used to transfer data between clusters whereas Sqoop can be used to transfer data only between Hadoop and RDBMS.

####  What are the limitations of importing RDBMS tables into Hcatalog directly?

There is an option to import RDBMS tables into Hcatalog directly by making use of –hcatalog –database option with the –hcatalog –table but the limitation to it is that there are several arguments like –as-avrofile , -direct, -as-sequencefile, -target-dir , -export-dir are not supported.


---------------------------------------------------
Hadoop Flume Interview Questions and Answers

####  Explain about the core components of Flume.

The core components of Flume are –

Event- The single log entry or unit of data that is transported.

Source- This is the component through which data enters Flume workflows.

Sink-It is responsible for transporting data to the desired destination.

Channel- it is the duct between the Sink and Source.

Agent- Any JVM that runs Flume.

Client- The component that transmits event to the source that operates with the agent.

####  Does Flume provide 100% reliability to the data flow?

Yes, Apache Flume provides end to end reliability because of its transactional approach in data flow.

####  How can Flume be used with HBase?

Apache Flume can be used with HBase using one of the two HBase sinks –

HBaseSink (org.apache.flume.sink.hbase.HBaseSink) supports secure HBase clusters and also the novel HBase IPC that was introduced in the version HBase 0.96.
AsyncHBaseSink (org.apache.flume.sink.hbase.AsyncHBaseSink) has better performance than HBase sink as it can easily make non-blocking calls to HBase.
Working of the HBaseSink –

In HBaseSink, a Flume Event is converted into HBase Increments or Puts. Serializer implements the HBaseEventSerializer which is then instantiated when the sink starts. For every event, sink calls the initialize method in the serializer which then translates the Flume Event into HBase increments and puts to be sent to HBase cluster.

Working of the AsyncHBaseSink-

AsyncHBaseSink implements the AsyncHBaseEventSerializer. The initialize method is called only once by the sink when it starts. Sink invokes the setEvent method and then makes calls to the getIncrements and getActions methods just similar to HBase sink. When the sink stops, the cleanUp method is called by the serializer.

####  Explain about the different channel types in Flume. Which channel type is faster?

The 3 different built in channel types available in Flume are-

MEMORY Channel – Events are read from the source into memory and passed to the sink.

JDBC Channel – JDBC Channel stores the events in an embedded Derby database.

FILE Channel –File Channel writes the contents to a file on the file system after reading the event from a source. The file is deleted only  after the contents are successfully delivered to the sink.

MEMORY Channel is the fastest channel among the three however has the risk of data loss. The channel that you choose completely depends on the nature of the big data application and the value of each event.

####  Which is the reliable channel in Flume to ensure that there is no data loss?

FILE Channel is the most reliable channel among the 3 channels JDBC, FILE and MEMORY.

####  Explain about the replication and multiplexing selectors in Flume.

Channel Selectors are used to handle multiple channels. Based on the Flume header value, an event can be written just to a single channel or to multiple channels. If a channel selector is not specified to the source then by default it is the Replicating selector. Using the replicating selector, the same event is written to all the channels in the source’s channels list. Multiplexing channel selector is used when the application has to send different events to different channels.

####  How multi-hop agent can be setup in Flume?

Avro RPC Bridge mechanism is used to setup Multi-hop agent in Apache Flume.

####  Does Apache Flume provide support for third party plug-ins?

Most of the data analysts use Apache Flume has plug-in based architecture as it can load data from external sources and transfer it to external destinations.

####  Is it possible to leverage real time analysis on the big data collected by Flume directly? If yes, then explain how.

Data from Flume can be extracted, transformed and loaded in real-time into Apache Solr servers using MorphlineSolrSink

####  Differentiate between FileSink and FileRollSink

The major difference between HDFS FileSink and FileRollSink is that HDFS File Sink writes the events into the Hadoop Distributed File System (HDFS) whereas File Roll Sink stores the events into the local file system.

Hadoop Flume Interview Questions and Answers for Freshers - Q.Nos- 1,2,4,5,6,10

Hadoop Flume Interview Questions and Answers for Experienced- Q.Nos-  3,7,8,9

Hadoop Zookeeper Interview Questions and Answers

####  Can Apache Kafka be used without Zookeeper?

It is not possible to use Apache Kafka without Zookeeper because if the Zookeeper is down Kafka cannot serve client request.

####  Name a few companies that use Zookeeper.

Yahoo, Solr, Helprace, Neo4j, Rackspace

####  What is the role of Zookeeper in HBase architecture?

In HBase architecture, ZooKeeper is the monitoring server that provides different services like –tracking server failure and network partitions, maintaining the configuration information, establishing communication between the clients and region servers, usability of ephemeral nodes to identify the available servers in the cluster.

####  Explain about ZooKeeper in Kafka

Apache Kafka uses ZooKeeper to be a highly distributed and scalable system. Zookeeper is used by Kafka to store various configurations and use them across the hadoop cluster in a distributed manner. To achieve distributed-ness, configurations are distributed and replicated throughout the leader and follower nodes in the ZooKeeper ensemble. We cannot directly connect to Kafka by bye-passing ZooKeeper because if the ZooKeeper is down it will not be able to serve the client request.

####  Explain how Zookeeper works

ZooKeeper is referred to as the King of Coordination and distributed applications use ZooKeeper to store and facilitate important configuration information updates. ZooKeeper works by coordinating the processes of distributed applications. ZooKeeper is a robust replicated synchronization service with eventual consistency. A set of nodes is known as an ensemble and persisted data is distributed between multiple nodes.

3 or more independent servers collectively form a ZooKeeper cluster and elect a master. One client connects to any of the specific server and migrates if a particular node fails. The ensemble of ZooKeeper nodes is alive till the majority of nods are working. The master node in ZooKeeper is dynamically selected by the consensus within the ensemble so if the master node fails then the role of master node will migrate to another node which is selected dynamically. Writes are linear and reads are concurrent in ZooKeeper.

#### List some examples of Zookeeper use cases.

Found by Elastic uses Zookeeper comprehensively for resource allocation, leader election, high priority notifications and discovery. The entire service of Found built up of various systems that read and write to   Zookeeper.
Apache Kafka that depends on ZooKeeper is used by LinkedIn
Storm that relies on ZooKeeper is used by popular companies like Groupon and Twitter.
#### How to use Apache Zookeeper command line interface?

ZooKeeper has a command line client support for interactive use. The command line interface of ZooKeeper is similar to the file and shell system of UNIX. Data in ZooKeeper is stored in a hierarchy of Znodes where each znode can contain data just similar to a file. Each znode can also have children just like directories in the UNIX file system.

Zookeeper-client command is used to launch the command line client. If the initial prompt is hidden by the log messages after entering the command, users can just hit ENTER to view the prompt.

#### What are the different types of Znodes?

There are 2 types of Znodes namely- Ephemeral and Sequential Znodes.

The Znodes that get destroyed as soon as the client that created it disconnects are referred to as Ephemeral Znodes.
Sequential Znode is the one in which sequential number is chosen by the ZooKeeper ensemble and is pre-fixed when the client assigns name to the znode.

####  What are watches?

Client disconnection might be troublesome problem especially when we need to keep a track on the state of Znodes at regular intervals. ZooKeeper has an event system referred to as watch which can be set on Znode to trigger an event whenever it is removed, altered or any new children are created below it.

####  What problems can be addressed by using Zookeeper?

In the development of distributed systems, creating own protocols for coordinating the hadoop cluster results in failure and frustration for the developers. The architecture of a distributed system can be prone to deadlocks, inconsistency and race conditions. This leads to various difficulties in making the hadoop cluster fast, reliable and scalable. To address all such problems, Apache ZooKeeper can be used as a coordination service to write correct distributed applications without having to reinvent the wheel from the beginning.


--------------------------------------------------------------
Hadoop Pig Interview Questions and Answers

####  What are different modes of execution in Apache Pig?

Apache Pig runs in 2 modes- one is the “Pig (Local Mode) Command Mode” and the other is the “Hadoop MapReduce (Java) Command Mode”. Local Mode requires access to only a single machine where all files are installed and executed on a local host whereas MapReduce requires accessing the Hadoop cluster.

####  Explain about co-group in Pig.

COGROUP operator in Pig is used to work with multiple tuples. COGROUP operator is applied on statements that contain or involve two or more relations. The COGROUP operator can be applied on up to 127 relations at a time. When using the COGROUP operator on two tables at once-Pig first groups both the tables and after that joins the two tables on the grouped columns.


-------------------------------------------------------------
Hadoop Hive Interview Questions and Answers

####  Explain about the SMB Join in Hive.

In SMB join in Hive, each mapper reads a bucket from the first table and the corresponding bucket from the second table and then a merge sort join is performed. Sort Merge Bucket (SMB) join in hive is mainly used as there is no limit on file or partition or table join. SMB join can best be used when the tables are large. In SMB join the columns are bucketed and sorted using the join columns. All tables should have the same number of buckets in SMB join.

####  How can you connect an application, if you run Hive as a server?

When running Hive as a server, the application can be connected in one of the 3 ways-

ODBC Driver-This supports the ODBC protocol

JDBC Driver- This supports the JDBC protocol

Thrift Client- This client can be used to make calls to all hive commands using different programming language like PHP, Python, Java, C++ and Ruby.

####  What does the overwrite keyword denote in Hive load statement?

Overwrite keyword in Hive load statement deletes the contents of the target table and replaces them with the files referred by the file path i.e. the files that are referred by the file path will be added to the table when using the overwrite keyword.

####  What is SerDe in Hive? How can you write your own custom SerDe?

SerDe is a Serializer DeSerializer. Hive uses SerDe to read and write data from tables. Generally, users prefer to write a Deserializer instead of a SerDe as they want to read their own data format rather than writing to it. If the SerDe supports DDL i.e. basically SerDe with parameterized columns and different column types, the users can implement a Protocol based DynamicSerDe rather than writing the SerDe from scratch.

We have further categorized Hadoop Hive Interview Questions for Freshers and Experienced-

Hadoop Hive Interview Questions and Answers for Freshers- Q.Nos-3

Hadoop Hive Interview Questions and Answers for Experienced- Q.Nos-1,2,4

Here are a few more frequently asked  Hadoop Hive Interview Questions and Answers for Freshers and Experienced

----------------------------------------------------
Hadoop YARN Interview Questions and Answers

#### What are the stable versions of Hadoop?

Release 2.7.1 (stable)

Release 2.4.1

Release 1.2.1 (stable)

#### What is Apache Hadoop YARN?

YARN is a powerful and efficient feature rolled out as a part of Hadoop 2.0.YARN is a large scale distributed system for running big data applications.

####  Is YARN a replacement of Hadoop MapReduce?

YARN is not a replacement of Hadoop but it is a more powerful and efficient technology that supports MapReduce and is also referred to as Hadoop 2.0 or MapReduce 2.

####  What are the additional benefits YARN brings in to Hadoop?

Effective utilization of the resources as multiple applications can be run in YARN all sharing a common resource.In Hadoop MapReduce there are seperate slots for Map and Reduce tasks whereas in YARN there is no fixed slot. The same container can be used for Map and Reduce tasks leading to better utilization.
YARN is backward compatible so all the existing MapReduce jobs.
Using YARN, one can even run applications that are not based on the MaReduce model

####  How can native libraries be included in YARN jobs?

There are two ways to include native libraries in YARN jobs-

1)  By setting the -Djava.library.path on the command line  but in this case there are chances that the native libraries might not be loaded correctly and there is possibility of errors.

2) The better option to include native libraries is to the set the LD_LIBRARY_PATH in the .bashrc file.

#### Explain the differences between Hadoop 1.x and Hadoop 2.x

In Hadoop 1.x, MapReduce is responsible for both processing and cluster management whereas in Hadoop 2.x processing is taken care of by other processing models and YARN is responsible for cluster management.
Hadoop 2.x scales better when compared to Hadoop 1.x with close to 10000 nodes per cluster.
Hadoop 1.x has single point of failure problem and whenever the NameNode fails it has to be recovered manually. However, in case of Hadoop 2.x StandBy NameNode overcomes the SPOF problem and whenever the NameNode fails it is configured for automatic recovery.
Hadoop 1.x works on the concept of slots whereas Hadoop 2.x works on the concept of containers and can also run generic tasks.

#### What are the core changes in Hadoop 2.0?

Hadoop 2.x provides an upgrade to Hadoop 1.x in terms of resource management, scheduling and the manner in which execution occurs. In Hadoop 2.x the cluster resource management capabilities work in isolation from the MapReduce specific programming logic. This helps Hadoop to share resources dynamically between multiple parallel processing frameworks like Impala and the core MapReduce component. Hadoop 2.x Hadoop 2.x allows workable and fine grained resource configuration leading to efficient and better cluster utilization so that the application can scale to process larger number of jobs.

####  Differentiate between NFS, Hadoop NameNode and JournalNode.

HDFS is a write once file system so a user cannot update the files once they exist either they can read or write to it. However, under certain scenarios in the enterprise environment like file uploading, file downloading, file browsing or data streaming –it is not possible to achieve all this using the standard HDFS. This is where a distributed file system protocol Network File System (NFS) is used. NFS allows access to files on remote machines just similar to how local file system is accessed by applications.

Namenode is the heart of the HDFS file system that maintains the metadata and tracks where the file data is kept across the Hadoop cluster.

StandBy Nodes and Active Nodes communicate with a group of light weight nodes to keep their state synchronized. These are known as Journal Nodes.

####  What are the modules that constitute the Apache Hadoop 2.0 framework?

Hadoop 2.0 contains four important modules of which 3 are inherited from Hadoop 1.0 and a new module YARN is added to it.

Hadoop Common – This module consists of all the basic utilities and libraries that required by other modules.
HDFS- Hadoop Distributed file system that stores huge volumes of data on commodity machines across the cluster.
MapReduce- Java based programming model for data processing.
YARN- This is a new module introduced in Hadoop 2.0 for cluster resource management and job scheduling.
CLICK HERE to read more about the YARN module in Hadoop 2.x.

####  How is the distance between two nodes defined in Hadoop?

Measuring bandwidth is difficult in Hadoop so network is denoted as a tree in Hadoop. The distance between two nodes in the tree plays a vital role in forming a Hadoop cluster  and is defined by the network topology and java interface DNStoSwitchMapping. The distance is equal to the sum of the distance to the closest common ancestor of both the nodes. The method getDistance(Node node1, Node node2) is used to calculate the distance between two nodes with the assumption that the distance from a node to its parent node is always 1.



We have further categorized Hadoop YARN Interview Questions for Freshers and Experienced-

Hadoop Interview Questions and Answers for Freshers - Q.Nos- 2,3,4,6,7,9
Hadoop Interview Questions and Answers for Experienced - Q.Nos- 1,5,8,10
What other questions do you have regarding your Hadoop career?

Hadoop Interview FAQ’s – An Interviewee Should Ask an Interviewer

For many hadoop job seekers, the question from the interviewer – “Do you have any questions for me?” indicates the end of a Hadoop developer job interview. It is always enticing for a Hadoop job seeker to immediately say “No” to the question for the sake of keeping the first impression intact.However, to land a hadoop job or any other job, it is always preferable to fight that urge and ask relevant questions to the interviewer. 

Asking questions related to the Hadoop technology implementation, shows your interest in the open hadoop job role and also conveys your interest in working with the company.Just like any other interview, even hadoop interviews are a two-way street- it helps the interviewer decide whether you have the desired hadoop skills they in are looking for in a hadoop developer, and helps an interviewee decide if that is the kind of big data infrastructure and hadoop technology implementation you want to devote your skills for foreseeable future growth in the big data domain.

Candidates should not be afraid to ask questions to the interviewer. To ease this for hadoop job seekers, DeZyre has collated few hadoop interview FAQ’s that every candidate should ask an interviewer during their next hadoop job interview-

####  What is the size of the biggest hadoop cluster a company X operates?

Asking this question helps a hadoop job seeker understand the hadoop maturity curve at a company.Based on the answer of the interviewer, a candidate can judge how much an organization invests in Hadoop and their enthusiasm to buy big data products from various vendors. The candidate can also get an idea on the hiring needs of the company based on their hadoop infrastructure.

####  For what kind of big data problems, did the organization choose to use Hadoop?

Asking this question to the interviewer shows the candidates keen interest in understanding the reason for hadoop implementation from a business perspective. This question gives the impression to the interviewer that the candidate is not merely interested in the hadoop developer job role but is also interested in the growth of the company.

####  Based on the answer to question no 1, the candidate can ask the interviewer why the hadoop infrastructure is configured in that particular way, why the company chose to use the selected big data tools and how workloads are constructed in the hadoop environment.

Asking this question to the interviewer gives the impression that you are not just interested in maintaining the big data system and developing products around it but are also seriously thoughtful on how the infrastructure can be improved to help business growth and make cost savings.

####  What kind of data the organization works with or what are the HDFS file formats the company uses?

The question gives the candidate an idea on the kind of big data he or she will be handling if selected for the hadoop developer job role. Based on the data, it gives an idea on the kind of analysis they will be required to perform on the data.

####  What is the most complex problem the company is trying to solve using Apache Hadoop?

Asking this question helps the candidate know more about the upcoming projects he or she might have to work and what are the challenges around it. Knowing this beforehand helps the interviewee prepare on his or her areas of weakness.

####  Will I get an opportunity to attend big data conferences? Or will the organization incur any costs involved in taking advanced hadoop or big data certification?

This is a very important question that you should be asking these the interviewer. This helps a candidate understand whether the prospective hiring manager is interested and supportive when it comes to professional development of the employee.

Hadoop Interview FAQ’s – Interviewer Asks an Interviewee

So, you have cleared the technical interview after preparing thoroughly with the help of the Hadoop Interview Questions shared by DeZyre. After an in-depth technical interview, the interviewer might still not be satisfied and would like to test your practical experience in navigating and analysing big data. The expectation of the interviewer is to judge whether you are really interested in the open position and ready to work with the company, regardless of the technical knowledge you have on hadoop technology.

There are quite a few on-going debates in the hadoop community, on the advantages of the various components in the hadoop ecosystem-- for example what is better MapReduce, Pig or Hive or Spark vs. Hadoop or when should a company use MapReduce over other alternative? etc. Interviewee and Interviewer should both be ready to answer such hadoop interview FAQs, as there is no right or wrong answer to these questions.The best possible way to answer these Hadoop interview FAQs is to explain why a particular interviewee favours an option. Answering these hadoop interview FAQs with practical examples as to why the candidate favours an option, demonstrates his or her understanding of the business needs and helps the interviewer judge the flexibility of the candidate to use various big data tools in the hadoop ecosystem.

Here are a few hadoop interview FAQs that are likely to be asked by the interviewer-

####  If you are an experienced hadoop professional then you are likely to be asked questions like  –

The number of nodes you have worked with in a cluster.
Which hadoop distribution have you used in your recent project.
Your experience on working with special configurations like High Availability.
The data volume you have worked with in your most recent project.
What are the various tools you used in the big data and hadoop projects you have worked on?
Your answer to these interview questions will help the interviewer understand your expertise in Hadoop based on the size of the hadoop cluster and number of nodes. Based on the highest volume of data you have handled in your previous projects, interviewer can assess your overall experience in debugging and troubleshooting issues involving huge hadoop clusters.

The number of tools you have worked with help an interviewer judge that you are aware of the overall hadoop ecosystem and not just MapReduce. To be selected, it all depends on how well you communicate the answers to all these questions.

####  What are the challenges that you faced when implementing hadoop projects?

Interviewers are interested to know more about the various issues you have encountered in the past when working with hadoop clusters and understand how you addressed them. The way you answer this question tells a lot about your expertise in troubleshooting and debugging hadoop clusters.The more issues you have encountered, the more probability there is, that you have become an expert in that area of Hadoop. Ensure that you list out all the issues that have trouble-shooted.

####  How were you involved in data modelling, data ingestion, data transformation and data aggregation?

You are likely to be involved in one or more phases when working with big data in a hadoop environment. The answer to this question helps the interviewer understand what kind of tools you are familiar with.

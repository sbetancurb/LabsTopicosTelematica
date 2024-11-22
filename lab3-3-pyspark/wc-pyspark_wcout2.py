from pyspark import SparkContext

sc = SparkContext()

# Leer archivos desde HDFS
files_rdd = sc.textFile("hdfs:///user/hadoop/datasets/gutenberg-small/*.txt")

# WordCount
wc_unsort = files_rdd.flatMap(lambda line: line.split()) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)

wc = wc_unsort.sortBy(lambda a: -a[1])

# Guardar resultado en HDFS
wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout2")

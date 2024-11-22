# Leer archivos desde HDFS
files_rdd = sc.textFile("hdfs:///user/hadoop/datasets/gutenberg-small/*.txt")

# WordCount: dividir palabras, contar ocurrencias y reducir
wc_unsort = files_rdd.flatMap(lambda line: line.split()) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)

# Ordenar por frecuencia descendente
wc = wc_unsort.sortBy(lambda a: -a[1])

# Mostrar las 10 palabras más frecuentes
for tupla in wc.take(10):
    print(tupla)

# Guardar el resultado en HDFS
wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout1")

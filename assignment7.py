import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
	sc = SparkContext("local", "Pyspark assignment 7")
	# create bag of words
	months = sc.textFile("input/input.txt").map(lambda line: line.split(","))
	result = months.map(lambda x: (str(x[0]), int(x[1]))).aggregateByKey((0, 0), lambda a,b: (a[0] + b,    a[1] + 1),
                                       											lambda a,b: (a[0] + b[0], a[1] + b[1]))
	final_result = sc.parallelize(result.mapValues(lambda x: x[0] / x[1]).collect())
	# result = months.map(lambda x: (str(x[0]), int(x[1]))).reduceByKey(lambda x,y: x + y)
	final_result.saveAsTextFile("output")
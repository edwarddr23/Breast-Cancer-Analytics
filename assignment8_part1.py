import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    sc = SparkContext("local", "pyspark avg temp")
    val = sc.textFile("input/input.txt").map(lambda line: line.split(","))
    result = val.map(lambda x: (str(x[1]), (float(x[2]), 1))).reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1]))
    avg_temp = result.mapValues(lambda x: (x[0]/x[1]))
    avg_temp.saveAsTextFile("output")
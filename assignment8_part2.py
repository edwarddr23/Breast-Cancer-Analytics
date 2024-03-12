import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    sc = SparkContext("local", "pyspark avg temp")
    val = sc.textFile("input/input.txt").map(lambda line: line.split(","))
    result = val.map(lambda x: (str(x[1]), 1)).reduceByKey(lambda a, b: a + b).filter(lambda x: str(x[0]) == 'M')
    result.saveAsTextFile("output")
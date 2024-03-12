import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    sc = SparkContext("local", "assignment 9")
    val = sc.textFile("input/input.txt").map(lambda line: line.split(",") if line.split(",")[0].isnumeric() else None)
    result = val.map(lambda x: (int(x[0]), int(x[1])))
    valid_males = result.filter(lambda x: x[0] >= 40 and x[0] <= 71 and x[1] == 0).count()
    valid_females = result.filter(lambda x: x[0] >= 30 and x[0] <= 60 and x[1] == 1).count()
    print(valid_males)
    print(valid_females)
    final = sc.parallelize(['Males within age 40-71: ' + str(valid_males), 'Females within age 30-60: ' + str(valid_females)])
    final.saveAsTextFile("output")
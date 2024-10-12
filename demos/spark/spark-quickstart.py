"""SimpleApp.py"""
import os
from pyspark.sql import SparkSession

# spark_home = os.getenv("SPARK_HOME")
spark_home = "/opt/module/spark-local"

logFile = f"{spark_home}/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()

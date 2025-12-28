"""
找出台北市、禮拜天晚上有看診的診所
"""

from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("filter-example") \
        .config("spark.home", "C:\\spark-3.3.2-bin-hadoop3") \
        .getOrCreate()

path = "..\\..\\範例資料\\ClinicMaster.csv"

df = spark.read.csv(path, header=True)

df.printSchema()

# df.show()

df.filter(df["縣市別代碼"] == "63000").show()

df.filter(df["縣市別代碼"] == "63000") \
  .filter(df["固定看診時段"].like("%星期日晚上看診%")) \
  .show()

spark.stop()
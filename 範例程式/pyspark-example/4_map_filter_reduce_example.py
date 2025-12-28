"""
計算在台北市內湖區、禮拜天晚上有看診的診所數量
"""
from itertools import count

from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("map-filter-reduce-example") \
        .config("spark.home", "C:\\spark-3.3.2-bin-hadoop3") \
        .getOrCreate()

path = "..\\..\\範例資料\\ClinicMaster.csv"

df = spark.read.csv(path, header=True)

df.printSchema()

# df.show()

# df.filter(df["縣市別代碼"] == "63000").show()

# 寫法一
# count = df.filter(df["縣市別代碼"] == "63000") \
#     .filter(df["固定看診時段"].like("%星期日晚上看診%")) \
#     .withColumn("短地址", df["地址"].substr(0, 6)) \
#     .filter(df["短地址"] == "臺北市內湖區") \
#     .count
#
# print(count)

# 寫法二
# df_short = df.filter(df["縣市別代碼"] == "63000") \
#     .filter(df["固定看診時段"].like("%星期日晚上看診%")) \
#     .withColumn("短地址", df["地址"].substr(0, 6))
#
# count = df_short.filter(df_short["短地址"] == "臺北市內湖區") \
#     .count()
#
# print(count)

spark.stop()
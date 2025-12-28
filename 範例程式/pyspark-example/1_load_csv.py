"""
載入衛福部開放資料的健保特約醫療診所清單
"""

from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("load-csv") \
        .config("spark.home", "C:\\spark-3.3.2-bin-hadoop3") \
        .getOrCreate()

path = "..\\..\\範例資料\\ClinicMaster.csv"

df = spark.read.csv(path, header=True)

df.printSchema()

df.show()

spark.stop()
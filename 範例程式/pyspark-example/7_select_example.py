"""
join 兩個 DataFrame 後，選取部分欄位進行顯示，並重新命名欄位
"""

import os
PYTHON_PATH = "C:\\Users\\cchua\\Codes\\am-spark-training\\範例程式\\pyspark-example\\.venv\\Scripts\\python.exe"
os.environ['PYSPARK_PYTHON'] = PYTHON_PATH


from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession \
        .builder \
        .appName("select-columns") \
        .config("spark.home", "C:\\spark-3.3.2-bin-hadoop3") \
        .config("spark.pyspark.python", PYTHON_PATH) \
        .config("spark.pyspark.driver.python", PYTHON_PATH) \
        .getOrCreate()

# 縣市別資料
data = [
    ("10001", "臺北縣"),
    ("10003", "桃園縣"),
    ("10017", "基隆市"),
    ("63000", "臺北市"),
    ("65000", "新北市"),
    ("68000", "桃園市"),
]

schema = StructType([
    StructField("代碼", StringType(), False),
    StructField("縣市名稱", StringType(), False),
])

city_df = spark.createDataFrame(data, schema)

# 驗證
city_df.printSchema()

# 診所資料
path = "..\\..\\範例資料\\ClinicMaster.csv"

clinic_df = spark.read.csv(path, header=True)

clinic_df.printSchema()

# 組合
joined_df = clinic_df.join(city_df, on=clinic_df["縣市別代碼"]==city_df["代碼"], how="inner")

joined_df.printSchema()
# joined_df.show()

# 選取需要的欄位
selected_df = joined_df.select("醫事機構名稱","電話", "地址", "縣市名稱")

selected_df.printSchema()

selected_df.show()

# alias
import pyspark.sql.functions as F

select_with_alias_df = joined_df.select(
    F.col("醫事機構名稱").alias("clinic_name"),
    F.col("電話").alias("tel"),
    F.col("地址").alias("address"),
    F.col("縣市名稱").alias("city"),
)

select_with_alias_df.printSchema()

select_with_alias_df.show()

spark.stop()
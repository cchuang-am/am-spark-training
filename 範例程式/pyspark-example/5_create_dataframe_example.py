"""
不載入任何資料，直接建立縣市代碼的 DataFrame

涉及 Python 資料轉換為 Spark DataFrame 的操作，因此需要特別設定 PySpark 使用的 Python 程式路徑
"""

import os
PYTHON_PATH = "C:\\Users\\cchua\\Codes\\am-spark-training\\範例程式\\pyspark-example\\.venv\\Scripts\\python.exe"
os.environ['PYSPARK_PYTHON'] = PYTHON_PATH


from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession \
        .builder \
        .appName("create-dataframe") \
        .config("spark.home", "C:\\spark-3.3.2-bin-hadoop3") \
        .config("spark.pyspark.python", PYTHON_PATH) \
        .config("spark.pyspark.driver.python", PYTHON_PATH) \
        .getOrCreate()

data = [
    ("10001", "臺北縣"),
    ("10002", "宜蘭縣"),
    ("10003", "桃園縣"),
    ("10004", "新竹縣"),
    ("10005", "苗栗縣"),
    ("10006", "臺中縣"),
    ("10007", "彰化縣"),
    ("10008", "南投縣"),
    ("10009", "雲林縣"),
    ("10010", "嘉義縣"),
    ("10011", "臺南縣"),
    ("10012", "高雄縣"),
    ("10013", "屏東縣"),
    ("10014", "臺東縣"),
    ("10015", "花蓮縣"),
    ("10016", "澎湖縣"),
    ("10017", "基隆市"),
    ("10018", "新竹市"),
    ("10019", "臺中市"),
    ("10020", "嘉義市"),
    ("10021", "臺南市"),
    ("09007", "連江縣"),
    ("09020", "金門縣"),
    ("63000", "臺北市"),
    ("64000", "高雄市"),
    ("65000", "新北市"),
    ("66000", "臺中市"),
    ("67000", "臺南市"),
    ("68000", "桃園市"),
]

schema = StructType([
    StructField("代碼", StringType(), False),
    StructField("縣市名稱", StringType(), False),
])

df = spark.createDataFrame(data, schema)

# 驗證
df.printSchema()

df.show()

spark.stop()
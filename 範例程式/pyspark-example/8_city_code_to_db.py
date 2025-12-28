"""
將縣市別代碼寫進資料庫裡
"""

import os
PYTHON_PATH = "C:\\Users\\cchua\\Codes\\am-spark-training\\範例程式\\pyspark-example\\.venv\\Scripts\\python.exe"
os.environ['PYSPARK_PYTHON'] = PYTHON_PATH


from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

H2_JDBC_PATH = "C:\\h2\\bin\\h2-2.1.214.jar"

spark = SparkSession \
        .builder \
        .appName("load-city-code-to-db") \
        .config("spark.home", "C:\\spark-3.3.2-bin-hadoop3") \
        .config("spark.pyspark.python", PYTHON_PATH) \
        .config("spark.pyspark.driver.python", PYTHON_PATH) \
        .config("spark.jars", H2_JDBC_PATH) \
        .config("spark.driver.extraClassPath", H2_JDBC_PATH) \
        .config("spark.executor.extraClassPath", H2_JDBC_PATH) \
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
    StructField("city_code", StringType(), False),
    StructField("city_name", StringType(), False),
])

df = spark.createDataFrame(data, schema)

# 驗證
df.printSchema()
# df.show()

# 寫入
# 格式為 jdbc:h2://<主機>:<port>/<資料庫名稱>
jdbc_conn_string = "jdbc:h2:tcp://localhost:9092/clinic"
df.write \
  .format("jdbc") \
  .mode("overwrite") \
  .option("driver", "org.h2.Driver") \
  .option("url", jdbc_conn_string) \
  .option("user", "sa") \
  .option("password", "") \
  .option("dbtable", "city_code") \
  .save()

print("done")

spark.stop()
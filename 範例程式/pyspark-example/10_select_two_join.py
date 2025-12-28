"""
將健保診所資料與縣市代碼查出後，在 Spark 裡做 join
"""

from pyspark.sql import SparkSession
import pyspark.sql.functions as F

H2_JDBC_PATH = "C:\\h2\\bin\\h2-2.1.214.jar"

spark = SparkSession \
        .builder \
        .appName("load-city-code-to-db") \
        .config("spark.home", "C:\\spark-3.3.2-bin-hadoop3") \
        .config("spark.jars", H2_JDBC_PATH) \
        .config("spark.driver.extraClassPath", H2_JDBC_PATH) \
        .config("spark.executor.extraClassPath", H2_JDBC_PATH) \
        .getOrCreate()

jdbc_conn_string = "jdbc:h2:tcp://localhost:9092/clinic"

clinic_df = spark.read \
    .format("jdbc") \
    .option("driver", "org.h2.Driver") \
    .option("url", jdbc_conn_string) \
    .option("user", "sa") \
    .option("password", "") \
    .option("dbtable", "clinic_raw") \
    .load()

city_code_df = spark.read \
    .format("jdbc") \
    .option("driver", "org.h2.Driver") \
    .option("url", jdbc_conn_string) \
    .option("user", "sa") \
    .option("password", "") \
    .option("dbtable", "city_code") \
    .load()

joined_df = clinic_df.join(
    city_code_df,
    on=clinic_df["縣市別代碼"]==city_code_df["city_code"],
    how="inner"
)

joined_df.printSchema()

joined_df.show()

spark.stop()
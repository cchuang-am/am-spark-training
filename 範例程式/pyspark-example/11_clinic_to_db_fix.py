"""
將衛福部開放資料的健保特約醫療診所清單的欄位名稱調整成英文，並寫入資料庫裡
"""

from pyspark.sql import SparkSession

H2_JDBC_PATH = "C:\\h2\\bin\\h2-2.1.214.jar"

spark = SparkSession \
        .builder \
        .appName("load-city-code-to-db") \
        .config("spark.home", "C:\\spark-3.3.2-bin-hadoop3") \
        .config("spark.jars", H2_JDBC_PATH) \
        .config("spark.driver.extraClassPath", H2_JDBC_PATH) \
        .config("spark.executor.extraClassPath", H2_JDBC_PATH) \
        .getOrCreate()

path = "..\\..\\範例資料\\ClinicMaster.csv"

df = spark.read.csv(path, header=True)

df.printSchema()

fixed_df = df.select(
    df["醫事機構代碼"].alias("clinic_id"),
    df["醫事機構名稱"].alias("clinic_name"),
    df["地址"].alias("clinic_address"),
    df["電話"].alias("clinic_phone"),
    df["縣市別代碼"].alias("city_code"),
    df["固定看診時段"].alias("open_time"))

fixed_df.printSchema()

jdbc_conn_string = "jdbc:h2:tcp://localhost:9092/clinic"
fixed_df.write \
  .format("jdbc") \
  .mode("overwrite") \
  .option("driver", "org.h2.Driver") \
  .option("url", jdbc_conn_string) \
  .option("user", "sa") \
  .option("password", "") \
  .option("dbtable", "clinic") \
  .save()

print("done")

spark.stop()
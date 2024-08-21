from pyspark.sql import SparkSession
from transformations import transform_data

# Criação de uma SparkSession
spark = SparkSession.builder \
    .appName("BigDataPipeline") \
    .getOrCreate()

# Leitura dos dados do HDFS
df = spark.read.csv("hdfs:///user/matheus/data.csv", header=True, inferSchema=True)

# Transformação dos dados
df_transformed = transform_data(df)

# Gravação dos resultados no HDFS
df_transformed.write.csv("hdfs:///user/matheus/output/total_sales_by_category", header=True)

# Fechar a sessão
spark.stop()
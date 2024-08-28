from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def processar_dados():
    spark = SparkSession.builder \
        .appName("BigDataHadoopPySparkExample") \
        .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
        .getOrCreate()

    df = spark.read.csv('hdfs://localhost:9000/user/hadoop/grandes_dados.csv', header=True, inferSchema=True)

    # Realizar operações no dataframe
    filtered_df = df.filter(col('coluna') > 100)

    # Convertendo para Pandas para facilitar a visualização
    pandas_df = filtered_df.toPandas()

    spark.stop()
    return pandas_df

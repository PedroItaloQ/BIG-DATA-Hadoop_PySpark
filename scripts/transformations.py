from pyspark.sql import DataFrame
from pyspark.sql.functions import sum

def transform_data(df: DataFrame) -> DataFrame:
    # Exemplo de agregação de dados
    df_transformed = df.groupBy("category").agg(sum("sales").alias("total_sales"))
    return df_transformed
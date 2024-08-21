from pyspark.sql import DataFrame

def clean_data(df: DataFrame) -> DataFrame:
    # Exemplo de remoção de valores nulos
    df_cleaned = df.dropna()
    return df_cleaned
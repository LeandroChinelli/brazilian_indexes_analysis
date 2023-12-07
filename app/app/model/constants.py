from pyspark.sql.types import StructType, StructField, DateType, IntegerType, FloatType

class Constants:

    STOCK_SYMBOL = '^BVSP'
    START_DATE = '1994-01-01'
    END_DATE = '2022-12-31'
    COLUMNS_BOVESPA = ['Close']

class Spark_Schemas:
  
    bovespa_schema = StructType([
                            StructField("Date", DateType(), True),
                            StructField("Close", FloatType(), True)
                            ])
    
    selic_schema = StructType([
                            StructField("Date", DateType(), True),
                            StructField("selic", FloatType(), True)
                            ])
    
    inflation_schema = StructType([
                            StructField("Date", DateType(), True),
                            StructField("ipca", FloatType(), True)
                            ])
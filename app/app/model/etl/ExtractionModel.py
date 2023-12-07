from pyspark.sql.dataframe import DataFrame

class ExtractionModel:
    bovespa_data: DataFrame
    selic_data: DataFrame
    inflation_data: DataFrame

    def __init__(self,bovespa_data
                    ,inflation_data
                    ,selic_data):
        self.bovespa_data = bovespa_data 
        self.inflation_data = inflation_data
        self.selic_data = selic_data 

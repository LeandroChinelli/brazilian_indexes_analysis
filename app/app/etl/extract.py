import yfinance as yf
from bcb import sgs 
from app.model.constants import Constants, Spark_Schemas
from app.model.etl.ExtractionModel import ExtractionModel

class Extraction:

    def extract(self, spark_session) -> ExtractionModel:
        bovespa_data = yf.download(Constants.STOCK_SYMBOL
                                ,start=Constants.START_DATE
                                ,end=Constants.END_DATE)
        columns_bovespa = Constants.COLUMNS_BOVESPA
        bovespa_data = bovespa_data[columns_bovespa]
        
        selic_data = sgs.get({'selic':432}
                             ,start=Constants.START_DATE
                             ,end=Constants.END_DATE)
        
        inflation_data = sgs.get({'ipca':433}
                             ,start=Constants.START_DATE
                             ,end=Constants.END_DATE)
        
        df_bovespa = spark_session.createDataFrame(bovespa_data.reset_index(),
                                                   schema=Spark_Schemas.bovespa_schema)
        df_bovespa = (df_bovespa.withColumnRenamed('Date','date')
                                .withColumnRenamed('Close','bovespa'))
        
        df_selic = spark_session.createDataFrame(selic_data.reset_index(),
                                                 schema=Spark_Schemas.selic_schema)
        df_selic = df_selic.withColumnRenamed('Date','date')
                      
        df_inflation = spark_session.createDataFrame(inflation_data.reset_index(),schema=Spark_Schemas.inflation_schema)
        df_inflation = df_inflation.withColumnRenamed('Date','date')
                      
        return ExtractionModel(df_bovespa, df_selic, df_inflation)

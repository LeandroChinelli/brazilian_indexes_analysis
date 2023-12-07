from pyspark.sql.dataframe import DataFrame

class TransformationModel:
    df_indexes: DataFrame
    correlation_matrix: DataFrame

    def __init__(self, df_indexes
                    ,correlation_matrix):
        self.df_indexes = df_indexes 
        self.correlation_matrix = correlation_matrix

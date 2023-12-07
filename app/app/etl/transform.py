from app.model.etl import ExtractionModel, TransformationModel
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler


class Transformation:
    
    def transform(self, extraction: ExtractionModel) -> TransformationModel:

        df_indexes = (extraction.bovespa_data.join(extraction.selic_data, 'date')
                                             .join(extraction.inflation_data, 'date'))
        
        vector_assembler = VectorAssembler(inputCols=['bovespa', 'selic', 'ipca'],
                                           outputCol='features')
        data_vector = vector_assembler.transform(df_indexes).select('features')

        correlation_matrix = Correlation.corr(data_vector, 'features').head()[0]

        return TransformationModel(df_indexes, correlation_matrix)


from app.model.etl import TransformationModel

class Load:
    
    def load(self, transformation: TransformationModel):
        transformation.df_indexes.show()
        print(transformation.correlation_matrix)
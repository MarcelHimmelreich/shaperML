from shapercore.Modules.metaclass.Module_Preprocessing import  Data
from sklearn.preprocessing import MinMaxScaler


class MinMaxScaler(Data):
    def __init__(self, feature_range= (0,1), copy=True):
        self._feature_range = feature_range
        self._copy = copy

    def requirement(self):
        """accept numeric values"""

    def execute(self, element):
        try:
            processor = MinMaxScaler(self._feature_range, self._copy)
            dataframe = element.get_dataframe()
            data = processor.fit_transform(dataframe.values)
            dataframe.values = data
            element.set_dataframe(dataframe)
        except Exception as error:
            print("Unable to perform min max scale")
            print("Error: " + str(error))

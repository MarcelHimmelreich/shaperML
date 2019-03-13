from shapercore.Modules.metaclass.Module_Preprocessing import  Data
from sklearn.preprocessing import MaxAbsScaler
from shapercore.Utility import Utility as Util


class MaxAbsScaler(Data):
    def __init__(self, copy=True):
        self._copy = copy

    def requirement(self):
        """accept numeric values"""

    def execute(self, element):
        try:
            processor = MaxAbsScaler(self._copy)
            dataframe = element.get_dataframe()
            data = processor.fit_transform(dataframe.values)
            dataframe.values = data
            element.set_dataframe(dataframe)
        except Exception as error:
            print("Unable to perform labelbinarize")
            print("Error: " + str(error))

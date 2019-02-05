from shapercore.Modules.metaclass.Module_Preprocessing import  Data
from sklearn.preprocessing import StandardScaler


class OneHotEncoder(Data):
    def __init__(self, copy=True, with_mean=True, with_std=True):
        self._copy = copy
        self._with_mean = with_mean
        self._with_std = with_std

    def requirement(self):
        """accept numeric and non-numeric values"""

    def execute(self, element):
        try:
            processor = StandardScaler(self._copy, self._with_mean, self._with_std)
            dataframe = element.get_dataframe()
            data = processor.fit_transform(dataframe.values)
            dataframe.values = data
            element.set_dataframe(dataframe)
        except Exception as error:
            print("Unable to perform standardize")
            print("Error: " + error)

from shapercore.Modules.metaclass.Module_Preprocessing import  Data
from sklearn.preprocessing import OneHotEncoder
from shapercore.Utility import Utility as Util


class OneHotEncoder(Data):
    def __init__(self, categories="auto", sparse=True, n_values="auto", categorical_features="all"):
        self._categories = categories
        self._sparse = sparse
        self._n_values = n_values
        self._categorical_features = categorical_features

    def requirement(self):
        """accept numeric values"""

    def execute(self, element):
        try:
            processor = OneHotEncoder(categories=self._categories, sparse=self._sparse, n_values=self._n_values,
                                      categorical_features=self._categorical_features)
            dataframe = element.get_dataframe()
            data = processor.fit_transform(dataframe.values)
            dataframe.values = data
            element.set_dataframe(dataframe)
        except Exception as error:
            print("Unable to perform one hot encode")
            print("Error: " + error)

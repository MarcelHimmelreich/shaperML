from shapercore.Modules.metaclass.Module_Preprocessing import  Data
from sklearn.preprocessing import Normalizer
from shapercore.Utility import Utility as Util


class Normalizer(Data):
    def requirement(self):
        """accept numeric values"""

    def execute(self, element):
        try:
            processor = Normalizer()
            dataframe = element.get_dataframe()
            data = processor.fit(dataframe.values)
            dataframe.values = data
            element.set_dataframe(dataframe)
        except Exception as error:
            print("Unable to perform normalize")
            print("Error: " + error)

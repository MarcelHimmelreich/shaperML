from shapercore.Modules.metaclass.Module_Preprocessing import  Data
from sklearn.preprocessing import LabelEncoder
from shapercore.Utility import Utility as Util


class LabelEncoder(Data):

    def requirement(self):
        """accept numeric and non-numeric values"""

    def execute(self, element):
        try:
            processor = LabelEncoder()
            dataframe = element.get_dataframe()
            data = processor.fit_transform(dataframe.values)
            classes = processor.classes_
            element.set_classes(classes)
            dataframe.values = data
            element.set_dataframe(dataframe)
        except Exception as error:
            print("Unable to perform label encoding")
            print("Error: " + str(error))

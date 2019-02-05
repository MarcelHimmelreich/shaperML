from shapercore.Modules.metaclass.Module_Preprocessing import  Data
from sklearn.preprocessing import LabelBinarizer


class LabelBinarizer(Data):
    def __init__(self, neg_label=0, pos_label=1, sparse_output = False):
        self._neg_label = neg_label
        self._pos_label = pos_label
        self._sparse_output = sparse_output

    def requirement(self):
        """accept numeric and non-numeric values"""

    def execute(self, element):
        try:
            processor = LabelBinarizer(self._neg_label, self._pos_label, self._sparse_output)
            dataframe = element.get_dataframe()
            data = processor.fit_transform(dataframe.values)
            classes = processor.classes_
            element.set_classes(classes)
            dataframe.values = data
            element.set_dataframe(dataframe)
        except Exception as error:
            print("Unable to perform label binarizing")
            print("Error: " + str(error))

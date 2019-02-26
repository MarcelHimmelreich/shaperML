from shapercore.Visitor.MetaClass.Element import Element


class Dataframe(Element):
    def __init__(self, name):
        self._dataframe = None
        self._name = name
        self._log = []
        self._datatype = []
        self._classes = None

    def accept(self, visitor):
        visitor.visit(self)

    def set_dataframe(self, dataframe):
        self._dataframe = dataframe

    def set_dataframe_values(self, value):
        self._dataframe.values = value

    def set_column_values(self, column, value):
        self._dataframe[column].values = value

    def set_column(self, column, value):
        self._dataframe[column] = value

    def set_name(self, name):
        self._name = name

    def set_log(self, log):
        self._log = log

    def set_datatype(self, datatype):
        self._datatype = datatype

    def set_classes(self, classes):
        self._classes = classes

    def get_dataframe(self):
        return self._dataframe

    def get_dataframe_values(self):
        return self._dataframe.values

    def get_column_values(self, column):
        return self._dataframe[column].values

    def get_column(self, column):
        return self._dataframe[column]

    def get_name(self):
        return self._name

    def get_log(self):
        return self._log

    def get_datatype(self):
        return self._datatype

    def get_classes(self):
        return self._classes

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

    def get_name(self):
        return self._name

    def get_log(self):
        return self._log

    def get_datatype(self):
        return self._datatype

    def get_classes(self):
        return self._classes

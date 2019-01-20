from shapercore.Visitor.MetaClass.Element import Element


class Dataframe(Element):
    def __init__(self, name):
        self._dataframe = None
        self._name = name

    def accept(self, visitor):
        pass

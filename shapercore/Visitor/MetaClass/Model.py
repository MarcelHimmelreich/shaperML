from shapercore.Visitor.MetaClass.Element import Element


class Model(Element):
    def __init__(self, name):
        self._model = None
        self._name = name

    def accept(self, visitor):
        pass

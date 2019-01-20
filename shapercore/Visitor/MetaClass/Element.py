from abc import abstractmethod
from shapercore.Visitor.MetaClass.MetaElement import MetaElement


class Element(metaclass=MetaElement):
    @abstractmethod
    def accept(self, visitor):
        pass

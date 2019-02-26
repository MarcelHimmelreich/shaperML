from abc import abstractmethod
from shapercore.Modules.metaclass.Module import Module


class Data(metaclass=Module):
    def __init__(self):
        pass


    @abstractmethod
    def visit(self, element):
        pass


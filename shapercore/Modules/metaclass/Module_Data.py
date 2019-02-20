from abc import abstractmethod
from shapercore.Modules.metaclass.Module import Module


class Data(metaclass=Module):
    def __init__(self):
        pass

    @abstractmethod
    def test_unit(self):
        pass

    @abstractmethod
    def execute(self, element):
        pass


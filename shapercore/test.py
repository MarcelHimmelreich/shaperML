from abc import abstractmethod


class Meta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


class Meta1(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


class Element(metaclass=Meta):

    @abstractmethod
    def accept(self, visitor):
        pass


class ConElement(Element):
    def accept(self, visitor):
        visitor.visit(self)


class Visitor(metaclass=Meta):

    @abstractmethod
    def visit(self, element):
        pass


class ConVisitor(Visitor):
    def visit(self, element):
        print("success")


class Visitor1(metaclass=Meta1):

    @abstractmethod
    def visit(self, element):
        pass


class ConVisitor1(Visitor1):
    def visit(self, element):
        print("success")


def main():
    v = ConVisitor()
    v1 = ConVisitor1()
    e = ConElement()
    e.accept(v)
    e.accept(v1)


if __name__ == "__main__":
    main()

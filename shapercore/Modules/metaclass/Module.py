class Module(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("Initialize Module: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

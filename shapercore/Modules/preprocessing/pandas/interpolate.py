from shapercore.Modules.metaclass.Module_Data import Data


class Interpolate(Data):
    def __init__(self, method="linear"):
        self._method = method

    def visit(self, featureset):
        try:
            data = featureset.get_featureset()
            if self._method == "median":
                data = data.fillna(data.median())
            else:
                data = data.interpolate(method=self._method)
            featureset.set_featureset(data)
        except Exception as error:
            Util.print_error("Unable to mask featureset: " + str(error))
            Util.print_detailed_error()


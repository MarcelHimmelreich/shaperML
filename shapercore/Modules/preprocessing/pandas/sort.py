from shapercore.Modules.metaclass.Module_Data import Data
from shapercore.Utility import Utility as Util


class Sort(Data):
    def __init__(self, mode="shuffle", column=None):
        self._mode = mode
        self._column = column

    def visit(self, element):
        try:
            data = element.get_dataframe()
            if self._mode == "shuffle":
                data = data.sample(frac=1)
            elif self._mode == "column":
                data = data.sort_values(by=self._column)
            elif self._mode == "index":
                data = data.sort_index()
            element.set_dataframe(data)
        except Exception as error:
            Util.print_error("Unable to sort featureset: " + str(error))
            Util.print_detailed_error()


import numpy as np
from shapercore.Modules.metaclass.Module_Data import Data
from shapercore.Utility import Utility as util


class JoinOperation(Data):
    """ Join a value to every item in feature """
    def __init__(self, column=None, value=""):
        self._column = column
        self._value = value

    def visit(self, featureset):
        try:
            featureset.set_dataframe_column(self._column,
                                                 np.char.join(self._value, featureset.get_column_values(self._column)))
        except Exception as error:
            util.print_error("Unable to add value to array")
            util.print_error(error)

import numpy as np
from shapercore.Modules.metaclass.Module_Data import Data
from shapercore.Utility import Utility as util



# Returns longest words number of given Data
class LongestWord(Data):
    """ Returns List with longest Words Count"""
    def __init__(self, column):
        self._column = column

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(max([len(x) for x in word]))
                else:
                    _preprocessed = max([len(x) for x in text])
                _result.append(_preprocessed)
            featureset.set_dataframe_column(self._column, np.asarray(list(_result))[:, np.newaxis])
        except Exception as error:
            util.print_error("Unable to create binary column")
            util.print_error(error)

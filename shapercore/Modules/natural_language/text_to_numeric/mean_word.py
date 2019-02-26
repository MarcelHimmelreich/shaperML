import numpy as np
from shapercore.Modules.metaclass.Module_Data import Data
from shapercore.Utility import Utility as util



# Returns mean words number of given Data
class MeanWord(Data):
    """ Returns List with mean Words Count"""
    def __init__(self, column):
        self._column = column

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(len(x) for x in word)
                else:
                    _preprocessed = [len(x) for x in text]
                _preprocessed = sum(_preprocessed) / len(_preprocessed)
                _result.append(_preprocessed)
            featureset.set_dataframe_column(self._column, np.asarray(list(_result))[:, np.newaxis])
        except Exception as error:
            util.print_error("Unable to create binary column")
            util.print_error(error)

import numpy as np
from shapercore.Modules.metaclass.Module_Data import Data
from shapercore.Utility import Utility as util



class StartWithNumber(Data):
    """ Creates a new Feature
    Binary feature if the data starts with a number"""
    def __init__(self, column):
        self._column = column

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(1 if word[0].isdigit() else 0)
                else:
                    _preprocessed = 1 if text[0].isdigit() else 0
                _result.append(_preprocessed)
            featureset.set_dataframe_column(self._column, np.asarray(list(_result))[:, np.newaxis])
        except Exception as error:
            util.print_error("Unable to create binary column")
            util.print_error(error)

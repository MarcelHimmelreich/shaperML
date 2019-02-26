import numpy as np
from shapercore.Modules.metaclass.Module_Data import Data
from shapercore.Utility import Utility as util


class CharacterSum(Data):
    """ Creates a new feature
    Calculates the sum of every text in a row in a feature"""
    def __init__(self, column):
        self._column = column

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(sum(len(x) for x in word))
                else:
                    _preprocessed = sum(len(x) for x in text)
                _result.append(_preprocessed)
            featureset.set_dataframe_column(self._column, np.asarray(list(_result))[:, np.newaxis])
        except Exception as error:
            util.print_error("Unable to create character sum of text")
            util.print_error(error)

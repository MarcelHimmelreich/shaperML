import numpy as np
import re
from shapercore.Utility import Utility as util
from shapercore.Modules.metaclass.Module_Data import Data


class RemoveChar(Data):
    """ Remove a specific character from every data in the feature"""
    def __init__(self, column, char):
        self._column = column
        self._char = char

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(self.remove(word))
                else:
                    _preprocessed = self.remove(text)
                _result.append(_preprocessed)
            _new_result = np.asarray(list(_result))[:, np.newaxis]
            _new_result = _new_result.reshape(featureset.get_column_values(self._column).shape)
            featureset.set_dataframe_column(self._column, _new_result)
        except Exception as error:
            util.print_error("Unable to tokenize column")
            util.print_error(error)

    def remove(self, string):
        return re.sub('[' + re.escape(''.join(self._char)) + ']', '', string)

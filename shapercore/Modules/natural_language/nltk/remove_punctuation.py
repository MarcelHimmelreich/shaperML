import numpy as np
import string
from shapercore.Utility import Utility as util
from shapercore.Modules.metaclass.Module_Data import Data


class RemovePunctuation(Data):
    """ Remove all the Punctations of the data in a feature"""
    def __init__(self, column):
        self._column = column

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                table = str.maketrans("", "", string.punctuation)
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(str(word).translate(table))
                else:
                    _preprocessed = str(text).translate(table)
                _result.append(_preprocessed)
            _new_result = np.asarray(list(_result))[:, np.newaxis]
            _new_result = _new_result.reshape(featureset.get_column_values(self._column).shape)
            featureset.set_dataframe_column(self._column, _new_result)
        except Exception as error:
            util.print_error("Unable to tokenize column")
            util.print_error(error)

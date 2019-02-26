import numpy as np
from nltk.stem import LancasterStemmer
from shapercore.Utility import Utility as util
from shapercore.Modules.metaclass.Module_Data import Data
porter = LancasterStemmer()


class Stemmer(Data):
    """ Stem all the data in the Feature
    Requires Data to be able to stem"""
    def __init__(self, column):
        self._column = column

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(porter.stem(x) for x in word)
                    _result.append(_preprocessed)
                else:
                    _preprocessed = [porter.stem(text)]
                    _result.append(_preprocessed)
            _new_result = np.asarray(list(_result))[:, np.newaxis]
            _new_result = _new_result.reshape(featureset.get_column_values(self._column).shape)
            featureset.set_dataframe_column(self._column, _new_result)
        except Exception as error:
            util.print_error("Unable to tokenize column")
            util.print_error(error)

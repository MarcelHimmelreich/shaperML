from nltk.util import ngrams
from shapercore.Utility import Utility as util
from shapercore.Modules.metaclass.Module_Data import Data


class NGram(Data):
    def __init__(self, column, n_gram_value):
        self._column = column
        self._n_gram_value = n_gram_value

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(self.n_gram(word))
                    _result.append(_preprocessed)
                else:
                    _preprocessed = self.n_gram(text)
                    print(_preprocessed)
                    _result.append(_preprocessed)
            featureset.set_dataframe_column(self._column, _result)
        except Exception as error:
            util.print_error("Unable to Create Word NGrams")
            util.print_error(error)

    def n_gram(self, text):
        return list(ngrams(text, self._n_gram_value))

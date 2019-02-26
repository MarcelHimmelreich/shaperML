from shapercore.Utility import Utility as util
from shapercore.Modules.metaclass.Module_Data import Data


class LowerCase(Data):
    """ Lowercase all the data in the feature """
    def __init__(self, column=None):
        self._column = column

    def visit(self, featureset):
        try:
            _result = []
            for text in featureset.get_column_values(self._column):
                if isinstance(text, list):
                    _preprocessed = []
                    for word in text:
                        _preprocessed.append(word.lower())
                    _result.append(_preprocessed)
                else:
                    _result.append(text.lower())
            featureset.set_dataframe_column(self._column, _result)
        except Exception as error:
            util.print_error("Unable to add value to array")
            util.print_error(error)

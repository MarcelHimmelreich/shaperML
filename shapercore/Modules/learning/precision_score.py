from shapercore.Modules.metaclass.Module_Learning import Data
from sklearn.metrics import precision_score
from shapercore.Utility import Utility as Util

class PrecisionScore(Data):
    def __init__(self, true, predict, average=None):
        self._true = true
        self._predict = predict
        self._average = average

    def visit(self, model):
        try:
            result = model.get_metric()
            result['PrecScore'] = precision_score(self._true, self._predict, average=self._average)
            model.set_metric(result)
        except Exception as error:
            Util.print_error("Unable to set estimator of Model")
            Util.print_error(error)
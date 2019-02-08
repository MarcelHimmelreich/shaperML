from shapercore.Modules.metaclass.Module_Learning import Data
from sklearn.metrics import accuracy_score


class AccuracyScore(Data):
    def __init__(self, true, predict):
        self._true = true
        self._predict = predict

    def visit(self, model):
        try:
            result = model.get_metric()
            result['AccScore'] = accuracy_score(self._true, self._predict)
            model.set_metric(result)
        except Exception as error:
            Util.print_error("Unable to set estimator of Model")
            Util.print_error(error)
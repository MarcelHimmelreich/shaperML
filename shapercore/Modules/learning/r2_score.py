from shapercore.Modules.metaclass.Module_Learning import Data
from sklearn.metrics import r2_score
from shapercore.Utility import Utility as Util

class R2Score(Data):
    def __init__(self, true, predict):
        self._true = true
        self._predict = predict

    def visit(self, model):
        try:
            result = model.get_metric()
            result['R2Score'] = r2_score(self._true, self._predict)
            model.set_metric(result)
        except Exception as error:
            Util.print_error("Unable to set estimator of Model")
            Util.print_error(error)
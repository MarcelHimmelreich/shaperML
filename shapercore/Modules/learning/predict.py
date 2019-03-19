from shapercore.Modules.metaclass.Module_Learning import Data
from shapercore.Utility import Utility as Util


class Predict(Data):
    def __init__(self, predict):
        self._predict = predict

    def visit(self, model):
        try:
            estimator = model.get_estimator()
            prediction = estimator.predict(self._predict)
            return prediction
        except Exception as error:
            Util.print_error("Unable to predict")
            Util.print_error(error)

from shapercore.Modules.metaclass.Module_Learning import Data
from shapercore.Utility import Utility as Util

class Fit(Data):
    def __init__(self, X, Y):
        self._X = X
        self._Y = Y

    def visit(self, model):
        try:
            estimator = model.get_estimator()
            estimator.fit(self._X, self._Y)
            model.set_estimator(estimator)
        except Exception as error:
            Util.print_error("Unable to fit estimator")
            Util.print_error(error)

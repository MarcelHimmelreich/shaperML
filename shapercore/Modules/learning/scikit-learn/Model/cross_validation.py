from shapercore.Modules.metaclass.Module_Learning import Data
from sklearn.model_selection import cross_validate


class CrossValidation(Data):
    def __init__(self, estimator, k_fold):
        self._estimator = estimator
        self._k_fold = int(k_fold)

    def visit(self, model):
        try:
            return cross_validate(self._estimator,
                                  model.get_x_train(),
                                  model.get_y_train(),
                                  cv=self._k_fold)

        except Exception as error:
            Util.print_error("Unable to calculate cross validation")
            Util.print_error(error)
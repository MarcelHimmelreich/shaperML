from shapercore.Modules.metaclass.Module_Learning import Data

# Classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier

# Regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.naive_bayes import MultinomialNB
from shapercore.Utility import Utility as Util


class SetEstimator(Data):
    """ Set the Estimator for Model """
    def __init__(self, estimator, parameter=None, return_value=False):
        self._estimator = estimator
        self._parameter = parameter
        self._learning_type = None
        self._return_value = return_value

    def visit(self, model):
        try:
            if self._return_value:
                return self.get_estimator(self._estimator)
            else:
                model.set_estimator(self.get_estimator(self._estimator))
                model.set_estimator_type(self._learning_type)
        except Exception as error:
            Util.print_error("Unable to set estimator of Model")
            Util.print_error(error)

    def get_estimator(self, estimator):
        # Classification
        if estimator == "RandomForestClassifier":
            self._learning_type = "classification"
            return RandomForestClassifier(verbose=True)
        elif estimator == "SVC":
            self._learning_type = "classification"
            return SVC(verbose=True)
        elif estimator == "LinearSVC":
            self._learning_type = "classification"
            return LinearSVC(verbose=True)
        elif estimator == "SGDClassifier":
            self._learning_type = "classification"
            return SGDClassifier(verbose=True)
        elif estimator == "KNeighborsClassifier":
            self._learning_type = "classification"
            return KNeighborsClassifier(verbose=True)
        elif estimator == "GaussianProcessClassifier":
            self._learning_type = "classification"
            return GaussianProcessClassifier(1.0*RBF(1.0))
        elif estimator == "DecisionTreeClassifier":
            self._learning_type = "classification"
            return DecisionTreeClassifier()
        elif estimator == "AdaBoostClassifier":
            self._learning_type = "classification"
            return AdaBoostClassifier()
        elif estimator == "MLPClassifier":
            self._learning_type = "classification"
            return MLPClassifier(verbose=True)
        elif estimator == "RandomForestClassifier":
            self._learning_type = "classification"
            return RandomForestClassifier(verbose=True)
        elif estimator == "QuadraticDiscriminantAnalysis":
            self._learning_type = "classification"
            return QuadraticDiscriminantAnalysis()

        # Regression
        if estimator == "RandomForestRegressor":
            self._learning_type = "regression"
            return RandomForestRegressor(verbose=True)
        elif estimator == "KNeighborsRegressor":
            self._learning_type = "regression"
            return KNeighborsRegressor(verbose=True)
        elif estimator == "MultinomialNB":
            self._learning_type = "regression"
            return MultinomialNB()
        elif estimator == "SVR":
            self._learning_type = "regression"
            return SVR(verbose=True)
        elif estimator == "Lasso":
            self._learning_type = "regression"
            return Lasso()
        elif estimator == "ElasticNet":
            self._learning_type = "regression"
            return ElasticNet()
        elif estimator == "Ridge":
            self._learning_type = "regression"
            return Ridge(alpha=1.0, solver="auto")
        elif estimator == "LogisticRegression":
            self._learning_type = "regression"
            return LogisticRegression(verbose=True)
        elif estimator == "SGDRegressor":
            self._learning_type = "regression"
            return SGDRegressor(verbose=True)

        """ Find Estimator by returning all estimators"""
        if estimator == "classification":
            self._learning_type = "classification"
            estimators = [SVC(), LinearSVC(), SGDClassifier(), KNeighborsClassifier(),
                          GaussianProcessClassifier(1.0 * RBF(1.0)), DecisionTreeClassifier(),
                          MLPClassifier()]
            return estimators
        elif estimator == "regression":
            self._learning_type = "regression"
            estimators = [RandomForestRegressor(), SVR(kernel='linear'), KNeighborsRegressor(), MultinomialNB(),
                          SVR(), Lasso(), ElasticNet(), Ridge(alpha=1.0, solver="auto"), LogisticRegression(),
                          SGDRegressor()]
            return estimators

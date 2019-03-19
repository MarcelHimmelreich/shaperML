from shapercore.Visitor.MetaClass.Element import Element


class Model(Element):
    def __init__(self, name):
        self._estimator = None
        self._model = None
        self._name = name
        self._metric = None
        self._estimator_type = None

    def accept(self, visitor):
        pass

    def set_estimator(self, estimator):
        self._estimator = estimator

    def set_model(self, model):
        self._model = model

    def set_metric(self, metric):
        self._metric = metric

    def set_estimator_type(self, type):
        self._estimator_type = type

    def get_estimator(self):
        return self._estimator

    def get_model(self):
        return self._model

    def get_metric(self):
        return self._metric

    def get_estimator_type(self):
        return self._estimator_type

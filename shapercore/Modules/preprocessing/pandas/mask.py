from shapercore.Modules.metaclass.Module_Data import Data
import pandas as pd

class Mask(Data):
    def __init__(self, condition, column=None):
        self._condition = condition
        self._column = column

    def visit(self, element):
        try:
            featureset = element.get_dataframe()
            if self._column is None:
                featureset = featureset.mask(eval(self._condition))
            else:
                feature = featureset[self._column]
                if feature.dtype == "object":
                    if isinstance(feature.iloc[0], (list, tuple, np.ndarray)):
                        feature = self.expand(pd.DataFrame(feature), self._column)
                        feature = feature.mask(eval(self._condition))
                        feature = list(feature.values)
                else:
                    feature = feature.mask(eval(self._condition))
                featureset[self._column] = feature
            element.set_dataframe(featureset)
        except Exception as error:
            Util.print_error("Unable to mask featureset: " + str(error))
            Util.print_detailed_error()

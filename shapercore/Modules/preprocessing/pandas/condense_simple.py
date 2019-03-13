from shapercore.Modules.metaclass.Module_Data import Data
from shapercore.Utility import Utility as Util
import pandas as pd
import numpy as np


class CondenseSimple(Data):
    def __init__(self, column, numeric_feature="median"):
        self._column = column
        self._numeric_feature = numeric_feature

    def visit(self, element):
        try:
            featureset_df = element.get_dataframe()

            # collect columns to restore initial column order in the end
            columns = list(featureset_df)

            # expand features, aggregate features, group features
            index_df = featureset_df[self._column] if type(self._column) is list else featureset_df[[self._column]]
            aggregated_groups = []
            for column in featureset_df:
                if featureset_df[column].dtype == "object":
                    if isinstance(featureset_df[column].iloc[0], (list, tuple, np.ndarray)):
                        group_df = self.expand(featureset_df, column, True)
                        group_idx = pd.concat([index_df, group_df], axis=1)
                        group_idx = group_idx.groupby(self._column).aggregate(self.select_numeric_op())
                        group_idx[column] = list(group_idx.values)
                        print(group_idx[[column]])
                        aggregated_groups.append(group_idx[[column]])

            print(featureset_df)
            featureset_df = featureset_df.groupby(self._column).aggregate(self.select_numeric_op())
            aggregated_groups.append(featureset_df)
            featureset_df = pd.concat(aggregated_groups, axis=1)
            featureset_df = featureset_df.reset_index()
            print(featureset_df)
            featureset_df = featureset_df.reindex(columns, axis=1)
            print(featureset_df)

            element.set_dataframe(featureset_df)

        except Exception as error:
            Util.print_error("Unable to condense Dataframe: " + str(error))
            Util.print_detailed_error()

    def select_numeric_op(self):
        if self._numeric_feature == "median":
            return np.median
        elif self._numeric_feature == "mean":
            return np.mean
        elif self._numeric_feature == "sum":
            return np.sum
        elif self._numeric_feature == "min":
            return np.min
        elif self._numeric_feature == "max":
            return np.max

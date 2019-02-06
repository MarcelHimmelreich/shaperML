from shapercore.Modules.metaclass.Module_Data import Data
import numbers


class FillEmptyCellsVisitor(Data):
    def __init__(self, column, feature_type, value):
        self._column = column
        self._type = feature_type
        self._value = value

    def visit(self, element):
        try:
            featureset_df = element.get_dataframe()

            # check if column is single-column or column group
            feature_vector = False
            target_column = featureset_df[self._column]
            if target_column.dtype == "object":
                if isinstance(target_column.iloc[0], (list, tuple, np.ndarray)):
                    feature_vector = True
                    target_column = self.expand(featureset_df, self._column, True)

            # TODO no option for feature vector with string features yet (compare numbers)
            if self._type == "string":
                target_column.fillna(self._value, inplace=True)

            if self._type == "number":
                if feature_vector:
                    for column in target_column:
                        self.fill_number_feature_cells(target_column[column])
                    featureset_df[self._column] = list(target_column[list(target_column)].values)
                else:
                    self.fill_number_feature_cells(target_column)

            element.set_dataframe(featureset_df)
        except Exception as error:
            Util.print_error("Unable to Group Features: " + str(error))
            Util.print_detailed_error()

    def fill_number_feature_cells(self, target_column):
        if isinstance(self._value, numbers.Number):
            target_column.fillna(self._value, inplace=True)
        elif self._value == "median":
            target_column.fillna(target_column.median(), inplace=True)
        elif self._value == "mean":
            target_column.fillna(target_column.mean(), inplace=True)
        elif self._value == "interpolate":
            target_column.interpolate(inplace=True)
        elif self._value == "zero":
            target_column.fillna(0, inplace=True)
        else:
            try:
                num = int(self._value)
            except ValueError:
                num = float(self._value)
            target_column.fillna(num, inplace=True)

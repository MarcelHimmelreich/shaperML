from shapercore.Modules.metaclass.Module_Data import Data
import pandas as pd

# Calculate arithmetic median for values
class Condense(Data):
    def __init__(self, column, sequential=False, numeric_feature="median", save_index=True, string_feature="join"):
        self._column = column
        self._sequential = sequential
        self._string_feature = string_feature
        self._numeric_feature = numeric_feature
        self._save_index = save_index

    def visit(self, element):
        try:
            featureset_df = element.get_dataframe()
            new_featureset = pd.DataFrame()
            if self._sequential is True:
                temp_dataframe = pd.DataFrame()
                temp_value = None
                temp_index = []
                for index, row in featureset_df.iterrows():
                    "Set first indexlist element"
                    if temp_value is None:
                        temp_value = row[self._column]
                        temp_index.append(index)
                    else:
                        "Check if value of column is in current row and add the row to new dataframe"
                        if temp_value != row[self._column]:
                            "Save the value from the selected column"
                            first_value_frame = pd.DataFrame({self._column: [temp_value]})

                            "Calculate the value for every column"
                            second_value_frame = self.select_numeric_feature(temp_dataframe)

                            "Transform Series Dataframe to Dataframe and transpose it"
                            second_value_frame = second_value_frame.to_frame().transpose()

                            "Add every column to dataframe"
                            for name, value in second_value_frame.iteritems():
                                first_value_frame[name] = value

                            "Add new row to dataframe"
                            new_featureset = new_featureset.append(first_value_frame, ignore_index=True)
                            temp_dataframe = pd.DataFrame()

                            "Add index to indexlist"
                            temp_index.append(index)
                            temp_value = row[self._column]
                    "Add Row to temporary dataframe"
                    temp_dataframe = temp_dataframe.append(featureset_df.iloc[index])

                "Save the value from the selected column"
                first_value_frame = pd.DataFrame({self._column: [temp_value]})

                "Calculate the value for every column"
                second_value_frame = self.select_numeric_feature(temp_dataframe)

                "Transform Series Dataframe to Dataframe and transpose it"
                second_value_frame = second_value_frame.to_frame().transpose()

                "Add every column to dataframe for last row"
                for name, value in second_value_frame.iteritems():
                    first_value_frame[name] = value

                new_featureset = new_featureset.append(first_value_frame, ignore_index=True)
            else:
                accumulate_list = featureset_df[self._column].unique()
                temp_unique_list = accumulate_list
                temp_index = []
                "Create Index list for unique values"
                for index, row in featureset_df.iterrows():
                    for value in temp_unique_list:
                        if value == row[self._column]:
                            temp_unique_list = temp_unique_list[temp_unique_list != value]
                            temp_index.append(index)
                            break
                for value in accumulate_list:
                    "Select all rows with value in column"
                    temp_dataframe = featureset_df.loc[featureset_df[self._column] == value]

                    "Save the value from the selected column"
                    first_value_frame = pd.DataFrame({self._column: [value]})

                    "Calculate the value for every column"
                    second_value_frame = self.select_numeric_feature(temp_dataframe)

                    "Transform Series Dataframe to Dataframe and transpose it"
                    second_value_frame = second_value_frame.to_frame().transpose()

                    "Add every column to dataframe"
                    for name, second_value in second_value_frame.iteritems():
                        first_value_frame[name] = second_value
                    new_featureset = new_featureset.append(first_value_frame, ignore_index=True)

            # Update Dataframe index
            if self._save_index:
                new_featureset["#index#"] = temp_index
                new_featureset = new_featureset.set_index("#index#")
                new_featureset.index.name = None

            "Reindexcolumns of the new dataframe with the old dataframe"
            new_featureset = new_featureset.reindex(columns=featureset_df.columns)
            element.set_dataframe(new_featureset)

        except Exception as error:
            Util.print_error("Unable to condense Dataframe: " + str(error))
            Util.print_detailed_error()

    def select_numeric_feature(self, dataframe):
        if self._numeric_feature == "median":
            return dataframe.median()
        elif self._numeric_feature == "mean":
            return dataframe.mean()
        elif self._numeric_feature == "sum":
            return dataframe.sum()
        elif self._numeric_feature == "min":
            return dataframe.min()
        elif self._numeric_feature == "max":
            return dataframe.max()


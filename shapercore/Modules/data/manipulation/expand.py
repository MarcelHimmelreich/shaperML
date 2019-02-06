from shapercore.Modules.metaclass.Module_Data import Data
import pandas as pd
import numpy as np

class Expand(Data):
    def __init__(self, column):
        self._column = column

    def execute(self, element):
        try:
            frame = element.get_dataframe()

            # get matrix
            matrix = frame[self._column]

            # get column names
            columns = []
            for i in range(len(matrix.iloc[0])):
                columns.append(self._column + "_" + str(i))

            # create dataframe from matrix
            matrix_df = pd.DataFrame(columns=columns)
            for index, col in enumerate(matrix):
                temp_frame = pd.DataFrame(np.array(col), index=columns)
                matrix_df = pd.concat([matrix_df, temp_frame.T], ignore_index=True)

            # create combined index
            frame_columns = list(frame)
            index = frame_columns.index(self._column)
            for column in reversed(columns):
                frame_columns.insert(index, column)
            frame_columns.remove(self._column)

            # concat dataframes and reindex
            matrix_df.set_index(frame.index, inplace=True)
            print(matrix_df.index)
            print(frame.index)

            frame = pd.concat([frame, matrix_df], axis=1)
            frame = frame.reindex(columns=frame_columns)

            print(frame.shape)
            element.set_dataframe(frame)

            '''
            dataframe = featureset.get_featureset()
            temp_index = dataframe.index.values
            new_dataframe = pd.DataFrame()
            print(self._column)
            matrix = dataframe[self._column]
            matrix_element_len = len(matrix.iloc[0])
            column_list = []
            for x in range(0, matrix_element_len):
                column_list.append(str(self._column) + "_" + str(x))

            temp_dataframe = pd.DataFrame(columns=column_list)
            for row in matrix:
                temp_frame = pd.DataFrame(np.array(row), index=column_list)
                temp_dataframe = pd.concat([temp_dataframe, temp_frame.T], ignore_index=True)

            new_dataframe = pd.concat([new_dataframe, temp_dataframe], axis=1)
            new_dataframe = new_dataframe.set_index(temp_index)
            dataframe = pd.concat([dataframe, new_dataframe], axis=1)
            dataframe = dataframe.drop(columns=str(self._column), axis=1)
            featureset.set_featureset(dataframe)
            '''

        except Exception as error:
            Util.print_error("Unable to Expand Feature: " + str(error))
            Util.print_detailed_error()


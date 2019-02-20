from shapercore.Modules.metaclass.Module_Data import Data
from shapercore.Utility import Utility as util
import numpy as np


class CheckString(Data):
    def __init__(self, column):
        super.__init__()
        self._column = column

    def test_unit(self):
        print("Todo")

    def execute(self, element):
        try:
            data_type = element.get_dataframe()[self._column].dtype
            if data_type == "object":
                data = element.get_dataframe()[self._column]
                for x in range(0, 1000):
                    if len(data) <= x:
                        continue

                    if isinstance(data.iloc[x], (list, tuple, np.ndarray)):
                        if len(data.iloc[x]) == 0:
                            continue
                        elif isinstance(data.iloc[x][0], str):
                            return False
                        elif isinstance(data.iloc[x][0], int):
                            return True
                        elif isinstance(data.iloc[x][0], float):
                            return True
                        else:
                            return False
                    elif isinstance(data.iloc[x], str):
                        return False
            elif isinstance(data_type, str):
                return False
            else:
                return False
        except Exception as error:
            util.print_error("Unable check numeric feature: " + str(error))
            util.print_detailed_error()

from shapercore.Modules.metaclass.Module_Data import Data
import numpy as np
from shapercore.Utility import Utility as Util


class Split(Data):
    def __init__(self, id_split, mode="sequential"):
        self._id_split = id_split
        self._mode = mode

    def visit(self, element):
        try:
            featuresets = {}
            data = element.get_dataframe()
            temp_data = []
            self.create_split_list(data.shape[0])
            for key, value in self._id_split.items():
                if self._mode == "sequential":
                    temp_data = data[:value]
                elif self._mode == "random":
                    temp_data = np.split(data, value)
                data = data.iloc[value:]
                featuresets[key] = temp_data
            return featuresets
        except Exception as error:
            Util.print_error("Unable to split Featureset in multiple Frames: " + str(error))
            Util.print_detailed_error()

    def create_split_list(self, row_count):
        dic_len = len(self._id_split)
        temp_dict = {}
        temp_row_count = row_count
        for key, value in self._id_split.items():
            temp_dict[key] = int(temp_row_count*value)
            temp_row_count = temp_row_count - temp_dict[key]
            dic_len = dic_len - 1
            for key2, value2 in self._id_split.items():
                if key != key2 and dic_len > 0:
                    self._id_split[key2] = self._id_split[key2] + value/dic_len
        self._id_split = temp_dict


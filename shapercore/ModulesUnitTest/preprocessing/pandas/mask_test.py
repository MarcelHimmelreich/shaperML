import unittest
import pandas
import numpy as np
import pandas.testing as test
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.preprocessing.pandas.mask import Mask


class CondenseTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        column_1 = "second_column"
        condition = "featureset > 3"
        test_data = pandas.DataFrame({column: [1, 2, 3, 4, 5],
                                  column_1: [5, 4, 3, 2, 1]})
        verify_data = pandas.DataFrame({column: [1, 2, 3, np.NaN, np.NaN],
                                  column_1: [np.NaN, np.NaN, 3, 2, 1]})

        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = Mask(condition)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

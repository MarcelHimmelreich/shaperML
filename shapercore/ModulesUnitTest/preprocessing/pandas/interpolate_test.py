import unittest
import pandas
import pandas.testing as test
import numpy as np
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.preprocessing.pandas.interpolate import Interpolate


class CondenseTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        column_1 = "second_column"
        mode_0 = "nearest"
        mode_1 = "linear"
        test_data = pandas.DataFrame({column: [1, 2, np.NaN, np.NaN, 5],
                                  column_1: [5.3, np.NaN, 3.5, np.NaN, 14.31]})
        verify_data = pandas.DataFrame({column: [1, 2, 2.0, 5.0, 5],
                                  column_1: [5.3, 5.3, 3.5, 3.5, 14.31]})

        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)

        visitor = Interpolate(mode_0)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

        verify_data = pandas.DataFrame({column: [1.0, 2.0, 3.0, 4.0, 5.0],
                                  column_1: [5.3, 4.4, 3.5, 8.905, 14.31]})

        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)

        visitor = Interpolate(mode_1)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

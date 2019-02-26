import unittest
import pandas
import pandas.testing as test
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.preprocessing.pandas.split import Split


class CondenseTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        ids = {"a": 0.2, "b": 0.4, "c": 0.4}
        test_data = pandas.DataFrame({column: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]})
        verify_data_0 = pandas.DataFrame({column: [0, 1]}, index=[0, 1])
        verify_data_1 = pandas.DataFrame({column: [2, 3, 4, 5]}, index=[2, 3, 4, 5])
        verify_data_2 = pandas.DataFrame({column: [6, 7, 8, 9]}, index=[6, 7, 8, 9])
        test_featureset = Dataframe()
        verify_featureset_0 = Dataframe()
        verify_featureset_1 = Dataframe()
        verify_featureset_2 = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset_0.set_dataframe(verify_data_0)
        verify_featureset_1.set_dataframe(verify_data_1)
        verify_featureset_2.set_dataframe(verify_data_2)

        visitor = Split(ids, "sequential")
        featuresets = visitor.visit(test_featureset)
        test.assert_frame_equal(featuresets["a"], verify_featureset_0.get_dataframe())
        test.assert_frame_equal(featuresets["b"], verify_featureset_1.get_dataframe())
        test.assert_frame_equal(featuresets["c"], verify_featureset_2.get_dataframe())


import unittest
import pandas
import pandas.testing as test
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.preprocessing.pandas.condense import Condense


class CondenseTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        column_1 = "test_column0"
        sequential = True
        test_data = pandas.DataFrame({column: [1, 2, 3, 4, 5],
                                      column_1: [5, 4, 3, 2, 1],
                                      "species": ["blue", "blue", "red", "red",  "blue"]})
        verify_data = pandas.DataFrame({column: [1.5, 3.5, 5],
                                        column_1: [4.5, 2.5, 1],
                                        "species": ["blue", "red", "blue"]}, index=[0, 2, 4])
        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = Condense("species", sequential)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

        test_data = pandas.DataFrame({column: [1, 2, 3, 4, 5],
                                      "species": ["blue", "blue", "red", "red", "blue"]})
        verify_data = pandas.DataFrame({column: [2, 3.5],
                                        "species": ["blue", "red"]}, index=[0, 2])
        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = Condense("species")
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

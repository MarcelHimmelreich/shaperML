import unittest
import pandas
import pandas.testing as test
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.preprocessing.pandas.sort import Sort


class CondenseTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        test_data = pandas.DataFrame({column: [3, 2, 1, 4, 5],
                                      "species": ["bb", "ba", "ab", "aa",  "bc"]})
        verify_data = pandas.DataFrame({column: [1, 2, 3, 4, 5],
                                        "species": ["ab", "ba", "bb", "aa", "bc"]}, index=[2, 1, 0, 3, 4])
        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)

        visitor = Sort("column", column)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

        test_data = pandas.DataFrame({column: [3, 2, 1, 4, 5],
                                      "species": ["bb", "ba", "ab", "aa",  "bc"]}, index=[3, 4, 2, 1, 0])
        verify_data = pandas.DataFrame({column: [5, 4, 1, 3, 2],
                                        "species": ["bc", "aa", "ab", "bb", "ba"]}, index=[0, 1, 2, 3, 4])
        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)

        visitor = Sort("index")
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

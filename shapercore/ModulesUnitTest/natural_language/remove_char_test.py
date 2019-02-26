import unittest
import pandas
import pandas.testing as test
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.natural_language.nltk.lowercase import RemoveChar


class RemoveCharTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        char = "s"
        test_data = pandas.DataFrame({column: ["TestString", "super", "wow"]})
        verify_data = pandas.DataFrame({column: ["TetString", "uper", "wow"]})
        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = RemoveChar(column, char)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

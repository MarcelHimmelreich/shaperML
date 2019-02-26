import unittest
import pandas
import pandas.testing as test
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.natural_language.nltk.lowercase import NGram


class NGramTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        n_gram_value = 3
        test_data = pandas.DataFrame({column: ["12345"]})
        verify_data = pandas.DataFrame({column: [[("1", "2", "3"), ("2", "3", "4"), ("3", "4", "5")]]})
        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = NGram(column, n_gram_value)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

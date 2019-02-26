import unittest
import pandas
import pandas.testing as test
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.natural_language.nltk.lowercase import Tokenizer


class LowercaseTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        test_data = pandas.DataFrame({column: ["Test String", "anothertest string",  "Another test string", "test"]})
        verify_data = pandas.DataFrame({column: [["Test", "String"], ["anothertest", "string"],
                                                 ["Another", "test", "string"], ["test"]]})
        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = Tokenizer(column)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

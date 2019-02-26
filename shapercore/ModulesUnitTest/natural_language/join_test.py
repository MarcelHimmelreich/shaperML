import unittest
import pandas
import pandas.testing as test
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.natural_language.nltk.lowercase import Join


class JoinTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        join_string = "!wow!"
        test_data = pandas.DataFrame({column: ["TestString", ["Test", "String"], ""]})
        verify_data = pandas.DataFrame({column: ["T!wow!e!wow!s!wow!t!wow!S!wow!t!wow!r!wow!i!wow!n!wow!g",
                                                 "Test!wow!String", ""]})
        test_featureset = Dataframe()
        verify_featureset = Dataframe()
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = Join(column, join_string)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

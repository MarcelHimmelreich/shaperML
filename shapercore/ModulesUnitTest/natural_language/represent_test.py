import unittest
import pandas
import pandas.testing as test
import os
from shapercore.Visitor.MetaClass.Dataframe import Dataframe
from shapercore.Modules.natural_language.nltk.lowercase import RepresentByWordlist


class RepresentByWordListTest(unittest.TestCase):

    def test_unit(self):
        column = "test_column"
        wordlist_0 = "Hallo"
        wordlist_1 = ["Hi", "Ok"]
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        wordlist_2 = os.path.join(__location__, "phrases.txt")
        mode_0 = "presence"
        mode_1 = "count"
        frompath = True
        test_data = pandas.DataFrame({column: ["Hallo hey was geht ab", "Hallo Hallo hallo", "hallo"]})
        verify_data = pandas.DataFrame({column: [[("1", "2", "3"), ("2", "3", "4"), ("3", "4", "5")]]})
        test_featureset = Dataframe()
        verify_featureset = Dataframe()

        test_data = pandas.DataFrame({column: ["Hallo hey was geht ab", "Hallo Hallo hallo", "hallo"]})
        verify_data = pandas.DataFrame({column:
                                            ["Hallo hey was geht ab", "Hallo Hallo hallo", "hallo"],
                                        str(wordlist_0+"_"+column+"_presence"):
                                            [1, 1, 0]})
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = RepresentByWordlist(column, wordlist_0, mode_0)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

        test_data = pandas.DataFrame({column: ["Hallo hey was geht ab Hi Ok", "Hallo Ok Hallo hallo", "hi Hi Hi hallo"]})
        verify_data = pandas.DataFrame({column:
                                            ["Hallo hey was geht ab Hi Ok", "Hallo Ok Hallo hallo", "hi Hi Hi hallo"],
                                        str(wordlist_1[0] + "_" + column + "_count"):
                                            [1, 0, 2],
                                        str(wordlist_1[1] + "_" + column + "_count"):
                                            [1, 1, 0]
                                        })
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = RepresentByWordlist(column, wordlist_1, mode_1)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

        test_data = pandas.DataFrame({column: ["Hallo hey was geht ab", "Hallo Hallo hallo", "hallo"]})
        verify_data = pandas.DataFrame({column:
                                            ["Hallo hey was geht ab", "Hallo Hallo hallo", "hallo"],
                                        str(wordlist_0 + "_" + column + "_count"):
                                            [1, 2, 0]})
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = RepresentByWordlist(column, wordlist_0, mode_1)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())


        "Load from Path"
        test_data = pandas.DataFrame({column: ["Hallo hey was geht ab", "Hallo Hallo hallo", "hallo"]})
        verify_data = pandas.DataFrame({column:
                                            ["Hallo hey was geht ab", "Hallo Hallo hallo", "hallo"],
                                        str("Hallo_" + column + "_presence"):
                                            [1, 1, 0],
                                        str("was geht_" + column + "_presence"):
                                            [1, 0, 0]
                                        })
        test_featureset.set_dataframe(test_data)
        verify_featureset.set_dataframe(verify_data)
        visitor = RepresentByWordlist(column, wordlist_2, mode_0, frompath)
        visitor.visit(test_featureset)
        test.assert_frame_equal(test_featureset.get_dataframe(), verify_featureset.get_dataframe())

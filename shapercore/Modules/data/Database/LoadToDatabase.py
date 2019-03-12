from shapercore.Modules.metaclass.Module_Data import Data
import os
import pandas as pd
from sqlalchemy import create_engine



class LoadToDatabase(Data):
    def __init__(self, table, column):
        self._table = table
        self._column = column
        # Postgres
        # set up postgres connection
        pwd = os.environ["SHARED_PASSWORD"]
        self.con = create_engine(
            "postgres://shared:{pwd}@postgres/shared".format(**locals()))

    def test_unit(self):
        pass

    def visit(self, element):


        # create a sample dataframe
        df_sample = pd.DataFrame(
            [
                [1, 2, 3],
                [4, 5, 6]
            ],
            columns=["a", "b", "c"])

        # Write
        df_sample.to_sql(name="sample", con=self.con, index=False)

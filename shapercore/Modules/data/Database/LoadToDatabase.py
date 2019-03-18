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

    def visit(self, element):
        dataframe = element.get_dataframe()

        # Write
        dataframe.to_sql(name="sample", con=self.con, index=False)

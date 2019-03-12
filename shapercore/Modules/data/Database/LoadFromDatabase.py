from shapercore.Modules.metaclass.Module_Data import Data
import os
import pandas as pd
from sqlalchemy import create_engine


class LoadFromDatabase(Data):
    def __init__(self, table, column):
        self._table = table
        self._column = column
        # Postgres
        # set up postgres connection
        self.pwd = os.environ["SHARED_PASSWORD"]
        self.con = create_engine("postgres://shared:{pwd}@postgres/shared".format(**locals()))

    def requirement(self):
        print("test")

    def unit_test(self):
        print("test")

    def visit(self):
        # Load
        pd.read_sql(sql="SELECT * FROM sample", con=con)




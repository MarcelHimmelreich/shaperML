from shapercore.Modules.metaclass.Module_Data import Data
import os
import pandas as pd
from sqlalchemy import create_engine


class LoadFromDatabase(Data):
    def __init__(self):
        # Postgres
        # set up postgres connection
        pwd = os.environ["SHARED_PASSWORD"]
        con = create_engine(
            "postgres://shared:{pwd}@postgres/shared".format(**locals()))

    def requirement(self):
        print("test")

    def unit_test(self):
        print("test")

    def execute(self):
        # Load
        pd.read_sql(sql="SELECT * FROM sample", con=con)




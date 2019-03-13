from fastapi import FASTAPI

#Visitor Pattern
from shapercore.Visitor.MetaClass.Dataframe import Dataframe

#Data Manipulation
from shapercore.Modules.data.Database.LoadFromDatabase import LoadFromDatabase
from shapercore.Modules.data.Database.LoadToDatabase import LoadToDatabase

#Natural Language
from shapercore.Modules.preprocessing.pandas.split import Split
from shapercore.Modules.preprocessing.pandas.sort import Sort
from shapercore.Modules.preprocessing.pandas.interpolate import Interpolate
from shapercore.Modules.preprocessing.pandas.mask import Mask
from shapercore.Modules.preprocessing.pandas.condense import Condense
from shapercore.Modules.preprocessing.pandas.condense_simple import CondenseSimple
from shapercore.Modules.preprocessing.pandas.fill_empty import FillEmptyCells

from shapercore.Modules.preprocessing.

#Required
# Table Column Parameter

app = FASTAPI()


@app.put("/preprocessing/split/{table, column}")
def split(table: str, column: str, id_split: dict, mode: str = "sequential"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    split = Split(id_split, mode)

    dataframe = download.visit(dataframe)

    # Return Dict of Feature sets
    # {name, data}
    dataframes = split.visit(dataframe)

    upload.visit(dataframes)


@app.put("/preprocessing/sort/{table, column}")
def sort(table: str, column: str, mode: str = "shuffle"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    sort = Sort(mode, column)

    dataframe = download.visit(dataframe)
    dataframe = sort.visit(dataframe)
    upload.visit(dataframe)


@app.put("/preprocessing/interpolate/{table, column}")
def interpolate(table: str, column: str, method: str = "linear"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    interpolate = Interpolate(method)

    dataframe = download.visit(dataframe)
    dataframe = interpolate.visit(dataframe)
    upload.visit(dataframe)


@app.put("/preprocessing/mask/{table, column}")
def mask(table: str, column: str, condition: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    mask = Mask(condition, column)

    dataframe = download.visit(dataframe)
    dataframe = mask.visit(dataframe)
    upload.visit(dataframe)


@app.put("/preprocessing/condense/{table, column}")
def condense(table: str, column: str, sequential: bool = False, numeric_feature: str = "median",
             save_index: bool = True, string_feature: str = "join"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    condense = Condense(column, sequential, numeric_feature, save_index, string_feature)

    dataframe = download.visit(dataframe)
    dataframe = condense.visit(dataframe)
    upload.visit(dataframe)


@app.put("/preprocessing/condense_simple/{table, column}")
def condense_simple(table: str, column: str, numeric_feature: str = "median"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    condense_simple = CondenseSimple(column, numeric_feature)

    dataframe = download.visit(dataframe)
    dataframe = condense_simple.visit(dataframe)
    upload.visit(dataframe)


@app.put("/preprocessing/fillempty/{table, column}")
def fillempty(table: str, column: str, feature_type: str, value: float):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    fillempty = FillEmptyCells( column, feature_type, value)

    dataframe = download.visit(dataframe)
    dataframe = fillempty.visit(dataframe)
    upload.visit(dataframe)

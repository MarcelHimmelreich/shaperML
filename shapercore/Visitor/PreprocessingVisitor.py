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

from shapercore.Modules.preprocessing.scikit.LabelBinarizer import LabelBinarizer
from shapercore.Modules.preprocessing.scikit.LabelEncode import LabelEncoder
from shapercore.Modules.preprocessing.scikit.MaxAbsScaler import MaxAbsScaler
from shapercore.Modules.preprocessing.scikit.minmaxscaler import MinMaxScaler
from shapercore.Modules.preprocessing.scikit.normalize import Normalizer
from shapercore.Modules.preprocessing.scikit.onehot import OneHotEncoder
from shapercore.Modules.preprocessing.scikit.standardscaler import StandardScaler


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


@app.put("/preprocessing/sort/{table, column}")
def labelbinarize(table: str, column: str, neg_label: int = 0, pos_label: int = 1, sparse_output: bool = False):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    binarize = LabelBinarizer(neg_label, pos_label, sparse_output)

    dataframe = download.visit(dataframe)
    dataframe = binarize.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/sort/{table, column}")
def labelencode(table: str, column: str, mode: str = "shuffle"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    encode = LabelEncoder(mode, column)

    dataframe = download.visit(dataframe)
    dataframe = encode.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/sort/{table, column}")
def maxabsscaler(table: str, column: str, copy: bool = True):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    scaler = MaxAbsScaler(copy)

    dataframe = download.visit(dataframe)
    dataframe = scaler.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/sort/{table, column}")
def minmaxscaler(table: str, column: str, feature_range: bytearray = (0, 1), copy:  bool = True):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    scaler = MinMaxScaler(feature_range, copy)

    dataframe = download.visit(dataframe)
    dataframe = scaler.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/sort/{table, column}")
def normalize(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    normalize = Normalizer()

    dataframe = download.visit(dataframe)
    dataframe = normalize.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/sort/{table, column}")
def onehot(table: str, column: str, categories: str = "auto", sparse: bool = True, n_values: str = "auto",
           categorical_features: str = "all"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    onehot = OneHotEncoder(categories, sparse, n_values, categorical_features)

    dataframe = download.visit(dataframe)
    dataframe = onehot.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/sort/{table, column}")
def standardscale(table: str, column: str, copy: bool = True, with_mean: bool = True, with_std=True):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    scaler = StandardScaler(copy, with_mean, with_std)

    dataframe = download.visit(dataframe)
    dataframe = scaler.visit(dataframe)
    upload.visit(dataframe)


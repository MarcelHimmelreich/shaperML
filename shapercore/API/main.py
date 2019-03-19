from fastapi import FASTAPI

#Visitor Pattern
from shapercore.Visitor.MetaClass.Dataframe import Dataframe

#Data Manipulation
from shapercore.Modules.data.Database.LoadFromDatabase import LoadFromDatabase
from shapercore.Modules.data.Database.LoadToDatabase import LoadToDatabase

#Natural Language
from shapercore.Modules.natural_language.nltk.join import JoinOperation
from shapercore.Modules.natural_language.nltk.lemmatize import Lemmatizer
from shapercore.Modules.natural_language.nltk.lowercase import LowerCase
from shapercore.Modules.natural_language.nltk.uppercase import UpperCase
from shapercore.Modules.natural_language.nltk.ngram import NGram
from shapercore.Modules.natural_language.nltk.remove_character import RemoveChar
from shapercore.Modules.natural_language.nltk.remove_punctuation import RemovePunctuation
from shapercore.Modules.natural_language.nltk.stem import Stemmer

from shapercore.Modules.natural_language.text_to_numeric.character_sum import CharacterSum
from shapercore.Modules.natural_language.text_to_numeric.longest_word import LongestWord
from shapercore.Modules.natural_language.text_to_numeric.mean_word import MeanWord
from shapercore.Modules.natural_language.text_to_numeric.start_with_number import StartWithNumber
from shapercore.Modules.natural_language.text_to_numeric.text_to_binary import TextToBinary

from shapercore.Modules.natural_language.language_processor.nl_processor import NaturalLanguageProcessor

#Preprocessing
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

#Learning
from shapercore.Modules.learning.accuracy_score import AccuracyScore
from shapercore.Modules.learning.cross_validation import CrossValidation
from shapercore.Modules.learning.f1_score import F1Score
from shapercore.Modules.learning.fit import Fit
from shapercore.Modules.learning.precision_score import PrecisionScore
from shapercore.Modules.learning.predict import Predict
from shapercore.Modules.learning.r2_score import R2Score
from shapercore.Modules.learning.recall_score import RecallScore
from shapercore.Modules.learning.set_estimator import SetEstimator

#Required
# Table Column Parameter

app = FASTAPI()


@app.put("/nl/lowercase/{table, column}")
def lowercase(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    lowercase = LowerCase()

    dataframe = download.visit(dataframe)
    dataframe = lowercase.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/uppercase/{table, column}")
def uppercase(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    uppercase = UpperCase()

    dataframe = download.visit(dataframe)
    dataframe = uppercase.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/lemmatize/{table, column}")
def lemmatize(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    lemmatize = Lemmatizer()

    dataframe = download.visit(dataframe)
    dataframe = lemmatize.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/stem/{table, column}")
def stem(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    stem = Stemmer()

    dataframe = download.visit(dataframe)
    dataframe = stem.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/ngram/{table, column}")
def ngram(table: str, column: str, value: int):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    ngram = NGram(n_gram_value=value)

    dataframe = download.visit(dataframe)
    dataframe = ngram.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/remove_punctuation/{table, column}")
def remove_punctuation(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    remove = RemovePunctuation()

    dataframe = download.visit(dataframe)
    dataframe = remove.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/remove_char/{table, column}")
def remove_character(table: str, column: str, char: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    remove = RemoveChar(char=char)

    dataframe = download.visit(dataframe)
    dataframe = remove.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/join/{table, column}")
def join(table: str, column: str, char: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    join = JoinOperation(value=char)

    dataframe = download.visit(dataframe)
    dataframe = join.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/character_sum/{table, column}")
def character_sum(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    sum = CharacterSum(column=column)

    dataframe = download.visit(dataframe)
    dataframe = sum.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/longest_word/{table, column}")
def longest_word(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    word = LongestWord(column=column)

    dataframe = download.visit(dataframe)
    dataframe = word.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/mean_word/{table, column}")
def mean_word(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    word = MeanWord(column=column)

    dataframe = download.visit(dataframe)
    dataframe = word.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/start_with_number/{table, column}")
def start_number(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    number = StartWithNumber(column=column)

    dataframe = download.visit(dataframe)
    dataframe = number.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/text_binary/{table, column}")
def text_binary(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    binary = TextToBinary(column=column)

    dataframe = download.visit(dataframe)
    dataframe = binary.visit(dataframe)
    upload.visit(dataframe)


@app.put("/nl/processor/{table, column}")
def nl_processor(table: str, column: str, extraction_target: str = "word", extraction_type: str = "bow",
                 measure: str = None, n_gram: bytearray = None):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    processor = NaturalLanguageProcessor(column, extraction_target, extraction_type, measure, n_gram)

    dataframe = download.visit(dataframe)
    dataframe = processor.visit(dataframe)
    upload.visit(dataframe)




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



@app.put("/preprocessing/labelencode/{table, column}")
def labelencode(table: str, column: str, mode: str = "shuffle"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    encode = LabelEncoder(mode, column)

    dataframe = download.visit(dataframe)
    dataframe = encode.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/maxscaler/{table, column}")
def maxabsscaler(table: str, column: str, copy: bool = True):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    scaler = MaxAbsScaler(copy)

    dataframe = download.visit(dataframe)
    dataframe = scaler.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/minscaler/{table, column}")
def minmaxscaler(table: str, column: str, feature_range: bytearray = (0, 1), copy:  bool = True):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    scaler = MinMaxScaler(feature_range, copy)

    dataframe = download.visit(dataframe)
    dataframe = scaler.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/normalize/{table, column}")
def normalize(table: str, column: str):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    normalize = Normalizer()

    dataframe = download.visit(dataframe)
    dataframe = normalize.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/onehot/{table, column}")
def onehot(table: str, column: str, categories: str = "auto", sparse: bool = True, n_values: str = "auto",
           categorical_features: str = "all"):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    onehot = OneHotEncoder(categories, sparse, n_values, categorical_features)

    dataframe = download.visit(dataframe)
    dataframe = onehot.visit(dataframe)
    upload.visit(dataframe)



@app.put("/preprocessing/scale/{table, column}")
def standardscale(table: str, column: str, copy: bool = True, with_mean: bool = True, with_std=True):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    scaler = StandardScaler(copy, with_mean, with_std)

    dataframe = download.visit(dataframe)
    dataframe = scaler.visit(dataframe)
    upload.visit(dataframe)


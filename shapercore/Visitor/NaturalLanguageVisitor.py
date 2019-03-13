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


@app.put("/nl/text_binary/{table, column}")
def nl_processor(table: str, column: str, extraction_target: str = "word", extraction_type: str = "bow",
                 measure: str = None, n_gram: bytearray = None):
    dataframe = Dataframe()
    download = LoadFromDatabase(table=table, column=column)
    upload = LoadToDatabase(table=table, column=column)
    processor = NaturalLanguageProcessor(column, extraction_target, extraction_type, measure, n_gram)

    dataframe = download.visit(dataframe)
    dataframe = processor.visit(dataframe)
    upload.visit(dataframe)




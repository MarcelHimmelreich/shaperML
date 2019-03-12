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

from fastapi import FASTAPI

#Visitor Pattern
from shapercore.Visitor.MetaClass.Dataframe import Dataframe

#Data Manipulation
from shapercore.Modules.data.Database.LoadFromDatabase import LoadFromDatabase
from shapercore.Modules.data.Database.LoadToDatabase import LoadToDatabase

#Natural Language
from shapercore.Modules.learning.sc

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
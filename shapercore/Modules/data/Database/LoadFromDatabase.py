from shapercore.Modules.metaclass.Module_Data import Data


class LoadFromDatabase(Data):
    def __init__(self):
        print("test")

    def requirement(self):
        print("test")

    def unit_test(self):
        print("test")

    def execute(self):
        print("test")

import os

import pandas as pd
from sqlalchemy import create_engine



#Postgres
# set up postgres connection
pwd = os.environ["SHARED_PASSWORD"]
con = create_engine(
    "postgres://shared:{pwd}@postgres/shared".format(**locals()))

# create a sample dataframe
df_sample = pd.DataFrame(
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    columns=["a", "b", "c"])

#Write
df_sample.to_sql(name="sample", con=con, index=False)

#Load
pd.read_sql(sql="SELECT * FROM sample", con=con)

#Minio
import os

from minio import Minio

# create a connection to the object store
minio_client = Minio(
    endpoint="minio:9000",
    access_key=os.environ["MINIO_ACCESS_KEY"],
    secret_key=os.environ["MINIO_SECRET_KEY"],
    secure=False
)

# write a sample file
with open("sample.txt", "w") as f:
    f.write("This is just a sample text")


#Write
# create a minio bucket
minio_client.make_bucket("sample-bucket")

# write the object to minio
minio_client.fput_object(
    bucket_name="sample-bucket",
    object_name="sample-file.txt",
    file_path="./sample.txt"
)

#Read
minio_client.get_object("sample-bucket", "sample-file.txt").data.decode()

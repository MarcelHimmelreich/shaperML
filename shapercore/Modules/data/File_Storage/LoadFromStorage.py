from shapercore.Modules.metaclass.Module_Data import Data
import os
from minio import Minio


# Minio
class LoadFromStorage(Data):
    def __init__(self):
        # create a connection to the object store
        self.minio_client = Minio(
            endpoint="minio:9000",
            access_key=os.environ["MINIO_ACCESS_KEY"],
            secret_key=os.environ["MINIO_SECRET_KEY"],
            secure=False
        )

    def unit_test(self):
        print("test")

    def execute(self):
        # Read
        self.minio_client.get_object("sample-bucket", "sample-file.txt").data.decode()

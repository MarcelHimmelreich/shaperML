from shapercore.Modules.metaclass.Module_Data import Data
import os
from minio import Minio


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
        # Write
        # create a minio bucket
        self.minio_client.make_bucket("sample-bucket")

        # write the object to minio
        self.minio_client.fput_object(
            bucket_name="sample-bucket",
            object_name="sample-file.txt",
            file_path="./sample.txt")




from shapercore.Modules.metaclass.Module_Data import Data
import os
from minio import Minio


class LoadFromStorage(Data):
    def __init__(self, bucket=None, object_name=None, file_path=None):
        self._bucket = bucket
        self._object_name = object_name
        self._file_path = file_path
        # create a connection to the object store
        self.minio_client = Minio(
            endpoint="minio:9000",
            access_key=os.environ["MINIO_ACCESS_KEY"],
            secret_key=os.environ["MINIO_SECRET_KEY"],
            secure=False)

    def execute(self):
        # Write
        # create a minio bucket
        self.minio_client.make_bucket(self._bucket)

        # write the object to minio
        self.minio_client.fput_object(
            bucket_name=self._bucket,
            object_name=self._object_name,
            file_path=self._file_path)




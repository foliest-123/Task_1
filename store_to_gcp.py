import os
from os import path
from google.cloud import storage

def upload_files_to_gcs(bucket_name, source_folder):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    my_files = os.listdir(source_folder)
    for filename in my_files:
        destination_blob_name = filename
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(os.path.join(source_folder, filename))

        print(f"{filename} uploaded to blob as {destination_blob_name}.")


bucket_name = "jsonfile_folder"
source_folder = r"C:\Task_1\json_data"
upload_files_to_gcs(bucket_name, source_folder)

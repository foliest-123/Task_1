import os
from google.cloud import storage

def upload_files_to_gcs(request):
    # Get the parameters from the HTTP request (if applicable)
    request_json = request()
    bucket_name = request.get("jsonfile_folder",)
    source_folder = request.get(r"C:\Task_1\json_data")

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    # List files in the local directory
    local_files = os.listdir(source_folder)

    for filename in local_files:
        local_file_path = os.path.join(source_folder, filename)

        # Upload the file to the Google Cloud Storage bucket
        destination_blob_name = filename
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file_path)

        print(f"{filename} uploaded to blob as {destination_blob_name}.")

    return "Files uploaded successfully."
storage_client = storage.Client()
bucket = storage_client.get_bucket("jsonfile_folder")
sample_request = {"bucket_name":bucket , "source_folder":r"C:\Task_1\json_data"}
upload_files_to_gcs(sample_request)
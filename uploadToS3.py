import boto3
import os

# this method upload the file at given path to S3 bucket
def upload_s3(file_name):
    s3_client=boto3.client('s3')

    bucket='pogen-upload'

    remote_file_name = str(file_name).split("/")
    remote_file_name = remote_file_name[len(remote_file_name) - 1]

    s3_client.upload_file(file_name, bucket, remote_file_name)

## this method will create the path for all the zip file present ,
def create_path(path):
    for file in os.listdir(path):
        if file.endswith(".zip"):
            file_path = os.path.join(path, file)
            print file_path

            try:
                upload_s3(file_path)

            except Exception as err:
                print("Failed to upload %s\n%s" % (file, err))
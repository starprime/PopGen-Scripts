import boto3



def upload_s3(path):
    s3_client=boto3.client('s3')

    bucket='pogen-upload'


    file_name=str('/home/sumit/Desktop/Popgen-processing/ready/Conneticut_SP/household_sample.csv.zip')
    remote_file_name = str(file_name).split("/")
    remote_file_name = remote_file_name[len(remote_file_name) - 1]

    tr=s3_client.upload_file(file_name, bucket, remote_file_name)

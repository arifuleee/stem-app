# full_stack_python/utils/s3.py

import boto3
from botocore.exceptions import NoCredentialsError

# Configure S3
S3_BUCKET = "aurbotbucket"
S3_REGION = "ap-south-1"
s3_client = boto3.client('s3')

def upload_video_to_s3(file_name, file_content):
    try:
        s3_client.put_object(Bucket=S3_BUCKET, Key=file_name, Body=file_content)
        video_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{file_name}"
        return video_url
    except NoCredentialsError:
        return None

def get_video_url(file_name):
    return f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{file_name}"

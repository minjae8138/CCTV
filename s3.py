import boto3
import os

BASE_DIR = os.getcwd()
IMAGE_DIR = os.path.join(BASE_DIR, '/home/pi/cctv/')
AWS_ACCESS_KEY_ID = "AKIA5VZTIAOJSE6WKUXQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_DEFAULT_REGION = "ap-northeast-3"
AWS_BUCKET_NAME = "team11-osaka-s3"

client = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_DEFAULT_REGION
                      )
s3 = boto3.resource('s3')

buckets = s3.Bucket(name=AWS_BUCKET_NAME)

file_path = os.path.join(IMAGE_DIR, 'cam.jpg')

key_name = "cam.jpg"

with open(file_path, 'rb') as data:
    buckets.upload_file(data.name, 'cam.jpg')
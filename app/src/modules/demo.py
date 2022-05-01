import boto3
import os

S3_ID = os.getenv('S3_USER_ID')
S3_KEY = os.getenv('S3_USER_KEY')
region = 'us-east-2'


def get_demo_telemetry():
    s3_client = boto3.client('s3', aws_access_key_id=S3_ID, aws_secret_access_key=S3_KEY, region_name=region)
    s3_client.download_file('skyboy-prod-demo-telemetry', 'TransformerMini-2022-04-24-171010.csv', 'demo-telemetry.csv')


import boto3
from AWSCloud.config import stores3
from imports import *


def load_video(video_name):
    s3 = boto3.client("s3", aws_access_key_id=stores3['aws_access_key_id'],
                        aws_secret_access_key=stores3['aws_secret_access_key'])
    try:
        s3.download_file('deep-fake-bucket', f'Check_Video/{video_name}.mp4', '../CheckVideo.mp4')
        print('File downloaded successfully')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print('The video file does not exist in the S3 bucket')
        else:
            print('An error occurred while downloading the video file from S3:', e)


def save_video(video_name):
    s3 = boto3.resource("s3", aws_access_key_id=stores3['aws_access_key_id'],
                        aws_secret_access_key=stores3['aws_secret_access_key'])
    s3.Bucket('deep-fake-bucket').upload_file(
        '../Result.mp4', f'Results/{video_name}_Result.mp4', ExtraArgs={'ContentType': "mp4"})

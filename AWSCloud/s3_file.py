import boto3
from AWSCloud.config import stores3

from imports import *


def save_img():
    s3 = boto3.resource("s3", aws_access_key_id=stores3['aws_access_key_id'],
                        aws_secret_access_key=stores3['aws_secret_access_key'])
    s3.Bucket('').upload_file(
        './Images/partner_creative/temp/template.png', f'partners/creative/{fileName}', ExtraArgs={'ContentType': "image/png"})
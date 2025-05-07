
import boto3
from PIL import Image
from io import BytesIO

class S3Helper:
    def __init__(self):
        self.client = boto3.client('s3')

    def get_object(self, bucket, key):
        return self.client.get_object(Bucket=bucket, Key=key)

    def upload_image(self, bucket, key, image, format, content_type):
        buffer = BytesIO()
        image.save(buffer, format)
        buffer.seek(0)
        self.client.put_object(Bucket=bucket, Key=key, Body=buffer, ContentType=content_type)

def load_image_from_s3(s3_helper, bucket, key):
    obj = s3_helper.get_object(bucket, key)
    body = obj['Body'].read()
    image = Image.open(BytesIO(body))
    content_type = obj['ContentType']
    format = image.format
    return image, content_type, format

def resize_image(image, size):
    resized = image.copy()
    resized.thumbnail(size)
    return resized

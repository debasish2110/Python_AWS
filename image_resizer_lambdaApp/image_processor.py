
import logging
from utils import S3Helper, load_image_from_s3, resize_image

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class ImageResizer:
    def __init__(self, dest_bucket, sizes):
        self.dest_bucket = dest_bucket
        self.sizes = sizes
        self.s3 = S3Helper()

    def process_event(self, event):
        for record in event['Records']:
            src_bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            logger.info(f"Received image: {key} from bucket: {src_bucket}")

            image, content_type, fmt = load_image_from_s3(self.s3, src_bucket, key)
            
            for size in self.sizes:
                width, height = map(int, size.lower().split("x"))
                resized = resize_image(image, (width, height))
                new_key = f"{size}/{key}"

                self.s3.upload_image(
                    bucket=self.dest_bucket,
                    key=new_key,
                    image=resized,
                    format=fmt,
                    content_type=content_type
                )

                logger.info(f"Saved resized image to: {new_key}")

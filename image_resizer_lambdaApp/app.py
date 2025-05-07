
from image_processor import ImageResizer
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DEST_BUCKET = os.environ.get("DEST_BUCKET")
SIZES = os.environ.get("SIZES", "300x300").split(",")

def lambda_handler(event, context):
    try:
        resizer = ImageResizer(dest_bucket=DEST_BUCKET, sizes=SIZES)
        resizer.process_event(event)
        return {"statusCode": 200, "body": "Images resized successfully."}
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return {"statusCode": 500, "body": str(e)}

from contextlib import asynccontextmanager

from aiobotocore.session import get_session

from app.core.config import settings
from app.logs.loggers import logger


class S3Client:
    def __init__(self, access_key_id: str, secret_access_key: str, endpoint_url: str, bucket_name: str):
        self.config = {
            "aws_access_key_id": access_key_id,
            "aws_secret_access_key": secret_access_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(self, filename: str, file: bytes):
        logger.info(f"Uploading file for filename {filename}")
        async with self.get_client() as client:
            await client.put_object(Bucket=self.bucket_name, Key=filename, Body=file)


s3_client = S3Client(
    access_key_id=settings.S3_ACCESS_KEY_ID,
    secret_access_key=settings.S3_SECRET_ACCESS_KEY,
    endpoint_url=settings.S3_ENDPOINT_URL,
    bucket_name=settings.S3_BUCKET_NAME,
)

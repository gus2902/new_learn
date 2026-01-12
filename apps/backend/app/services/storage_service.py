import boto3
from botocore.config import Config

from app.core.config import settings


def get_r2_client():
    return boto3.client(
        "s3",
        endpoint_url=settings.r2_endpoint,
        aws_access_key_id=settings.r2_access_key,
        aws_secret_access_key=settings.r2_secret_key,
        config=Config(signature_version="s3v4"),
        region_name="auto",
    )


async def upload_to_r2(file_content: bytes, file_key: str, content_type: str = "text/html") -> str:
    client = get_r2_client()
    client.put_object(
        Bucket=settings.r2_bucket,
        Key=file_key,
        Body=file_content,
        ContentType=content_type,
    )
    return f"{settings.r2_endpoint}/{settings.r2_bucket}/{file_key}"


async def get_from_r2(file_key: str) -> bytes:
    client = get_r2_client()
    response = client.get_object(
        Bucket=settings.r2_bucket,
        Key=file_key,
    )
    return response["Body"].read()

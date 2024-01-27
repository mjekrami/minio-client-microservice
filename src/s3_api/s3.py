from fastapi.exceptions import HTTPException
from minio import Minio
from minio.error import S3Error, InvalidResponseError


class S3Client(Minio):
    """Minio client wrapper"""

    def __init__(self, endpoint, access_key, secret_key, use_ssl: bool = False):
        self.client = Minio(endpoint, access_key, secret_key, secure=use_ssl)

    def bucket_exists(self, bucket_name) -> bool:
        try:
            return self.client.bucket_exists(bucket_name)
        except S3Error:
            raise HTTPException(500, "error connecting to the s3")
        except InvalidResponseError:
            raise HTTPException(
                500,
                "invalid response type. make sure you are connceted to the right port",
            )

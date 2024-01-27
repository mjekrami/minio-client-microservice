import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from s3_api import S3Client

app = FastAPI()
s3_client = S3Client(
    "localhost:9000",
    "vKGrDlFl1IQSCmCrczQY",
    "LaVUeuCiAzvbJgtQGmpbO6BFlC6e06BbfVIzRVle",
    False,
)


@app.get("/")
def index():
    return {"hello": "world"}


@app.get("/{bucket_name}")
def if_bucket_exists(bucket_name: str):
    return s3_client.bucket_exists(bucket_name)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

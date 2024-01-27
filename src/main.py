import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

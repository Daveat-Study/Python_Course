from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mesage": "Hello World"}

@app.get("/post")
async def get_post():
    return {"data": "This is post"}
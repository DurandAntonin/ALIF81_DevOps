from fastapi import FastAPI, status

app = FastAPI()

@app.get("/sayHello", status_code=status.HTTP_200_OK)
def say_hello():
    return {"message": "Hello World"}
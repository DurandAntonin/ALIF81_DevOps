from fastapi import FastAPI, status


from src.routes import characters_route
app = FastAPI()

app.include_router(characters_route.route)

@app.get("/sayHello", status_code=status.HTTP_200_OK)
def say_hello():
    return {"message": "Hello World"}
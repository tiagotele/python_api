from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter
from fastapi.testclient import TestClient

app = FastAPI()
Instrumentator().instrument(app).expose(app)

about_counter = Counter(
    "about_call",
    "Number of times about endpoint was called.",
    ['about']
)

@app.get("/")
async def root():
    return {"Message": "Hello World"}

@app.get("/about")
async def about():
    about_counter.labels('about').inc()
    return {"About": "Unifametro class"}

client = TestClient(app)
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

app = FastAPI()
Instrumentator().instrument(app).expose(app)

about_counter = Counter(
    "about_call",
    "Number of times about endpoint was called.",
    labelnames=("about")
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def root():
    about_counter.labels('about').inc()
    return {"About": "Unifametro class"}

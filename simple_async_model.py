import asyncio
from concurrent.futures.process import ProcessPoolExecutor
from http import HTTPStatus
from typing import Dict, List
from uuid import UUID, uuid4
import time
from fastapi import BackgroundTasks, FastAPI, Request, UploadFile, File
from pydantic import BaseModel, Field

from iris import Iris
import pickle
import pandas as pd

app = FastAPI()

class Job(BaseModel):
    uid: UUID = Field(default_factory = uuid4)
    status: str = "in_progress"
    result: str = None

jobs: Dict[UUID, Job] = {}

with open('./rf.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

@app.get('/')
def index():
    return {"Message":"Welcome"}

def model(tgs: List[list] = []):
    prediction = classifier.predict([tgs])
    time.sleep(10)
    return str(prediction)

async def run_in_process(fn, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(app.state.executor, fn, *args)

async def start_modelling_task(uid: UUID, tgs: List[list] = []) -> None:
    jobs[uid].result = await run_in_process(model, tgs)
    jobs[uid].status = 'complete'


@app.post("/predict", status_code = HTTPStatus.ACCEPTED)
async def task_handler(data:Iris, background_tasks: BackgroundTasks):
    data = data.dict()
    print("in the prediction")
    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    petal_length = data['petal_length']
    petal_width = data['petal_width']
    new_task = Job()
    jobs[new_task.uid] = new_task
    background_tasks.add_task(start_modelling_task, new_task.uid, [sepal_length, sepal_width, petal_length, petal_width])
    return new_task

@app.get("/status/{uid}")
async def status_handler(uid: UUID):
    return jobs[uid]

@app.on_event("startup")
async def startup_event():
    app.state.executor = ProcessPoolExecutor()

@app.on_event("shutdown")
async def on_shutdown():
    app.state.executor.shutdown()

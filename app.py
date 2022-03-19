import os
import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Script(BaseModel):
    filepath: str
    device: str

@app.post("/")
async def get_script_content(script: Script):
    filepath = f'iot_scripts/{script.device}/{script.filepath}'
    with open(filepath,'r') as f:
        content = f.read()
    return {
        'script_content': content
        }

@app.get("/script_list")
async def get_script_list():
    dir_list = dict()
    rootdir = 'iot_scripts'
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            dir_list[file] = os.listdir(d)

    return ({
        "dir_list": dir_list
        })

@app.post("/add_script")
async def add_script(script: Script):
    pass

@app.post("/commit_script")
async def commit_script(script: Script):
    
    return {
        "message" : "Commit Code"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
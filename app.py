import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import *
from iot_scripts import NodeMCUFunctions, ArduinoFunctions

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# Run IOT Devices

@app.post("/run_firmata")
async def run_firmata(device: str):
    ArduinoFunctions().blink()
    return "Successful"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
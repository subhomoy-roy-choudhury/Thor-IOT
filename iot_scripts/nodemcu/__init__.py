import pyfirmata
import time
import json
import os

class NodeMCUFunctions(object):
    def __init__(self) -> None:
        self.path = 'iot_scripts/nodemcu'
        self.details = self.parse_details_json()
        self.board = pyfirmata.Arduino(self.details['port'])
        print("Communication Successfully started")
        self.list = {
            "blink" : self.blink()
        }
    
    def parse_details_json(self):
        with open(os.path.join(self.path,'details.json')) as f:
            data = json.load(f)
            return data

    def show_list(self):
        return self.list.keys()

    def blink(self):
        while True:
            self.board.digital[13].write(1)
            time.sleep(1)
            self.board.digital[13].write(0)
            time.sleep(1)

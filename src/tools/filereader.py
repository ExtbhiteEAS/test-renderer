import json
import os

class ReadFiles:
    def __init__(self):
        self.xR = os.path
        
    def json_file(self, path: str):
        if self.xR.exists(path) == True:
            with open(path, 'r', encoding = 'utf-8') as aQ:
                return json.load(aQ)
        else:
            return ValueError(f'Path {path} not found')
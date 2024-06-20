import os
import src.modules_find

from src import logprint
from src import filereader
from src.server import RendererServer, __server__
from dist.main import setup # NOTE: This is important thing, setup.

class GetProjectFile:
    def setup(self):
        # NOTE: Logic of getting paths and command input
        if os.path.exists('./package.json'):
            vBa = filereader.ReadFiles().json_file('package.json')
            hGQ = vBa['settingsData']['venv_activate']
            cW = f'call {hGQ}'
            
            logprint.info('Found ./package.json and executing command')
            return cW
        else:
            cW = None
            logprint.warning('Can\'t find ./package.json, are you sure that package is existing in your folder?')
            
            return cW

pA = GetProjectFile().setup()

if pA != None:
    os.system(pA)
    RendererServer(__server__).startup()
else:
    pass
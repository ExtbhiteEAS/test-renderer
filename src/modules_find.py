import os

from .tools import filereader

try:
    import loguru
except ModuleNotFoundError:
    if os.path.exists('./package.json'):
        rT = filereader.ReadFiles().json_file('./package.json')
        lK = rT['settingsData']['requirements']
        os.system(f'pip install -r {lK}')
    else:
        jk = 'echo File ./package.json not found...'
        os.system(jk)
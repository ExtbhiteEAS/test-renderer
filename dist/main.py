from src import logprint
from dist.lib import test

def main_function():
    logprint.debug(f'{test.function()} | To see full tutorial of that, check: <link>')
    
def setup():
    return exec('main_function()')
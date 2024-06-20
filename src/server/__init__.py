from aiohttp import web
from .handlers import *
from src.tools.logger import logprint

__server__ = web.Application()

class RendererServer:
    def __init__(self, client: web.Application) -> None:
        self.client = client
        
    def add_routes(self, routes: web.RouteTableDef):
        logprint.debug(f'Adding routes: {routes}')
        return self.client.add_routes(routes)
    
    def startup(self):
        logprint.info('Starting up the server')
        
        try:
            self.add_routes(DefaultRoutes.routes) # Default (required)
            
            return web.run_app(self.client, host = '127.0.0.1', port = 4444)
        except Exception as e:
            logprint.error(f'Error while tried to startup server: {e}')
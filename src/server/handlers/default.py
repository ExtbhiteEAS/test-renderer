from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import json_response
from src.tools.logger import logprint
from dist.main import setup
from dist.manifest import configure

import base64
import os

class DefaultRoutes:
    routes = web.RouteTableDef()
    
    @routes.get('/')
    async def api_main(request: Request):
        logprint.info('Request on \'/\'')
        
        return web.Response(
            text = 'Your renderer thing. Welcome.'
        )
    
    @routes.get('/api/v1/renderer')
    async def api_renderer(request: Request):
        try:
            with open('./dist/main.py', 'r', encoding = 'utf-8') as file_data:
                data = file_data.read()
                
            buffer_data = base64.b64encode(bytes(data, encoding = 'utf-8'))
        
            # NOTE: Checking of extras
            if configure['extras'] != []:
                extras_data = []
                
                for cycle_extra in range(0, len(configure['extras'])):
                    for path_extra in configure['extras'][cycle_extra]:
                        if os.path.exists(path_extra):
                            with open(path_extra, 'r', encoding = 'utf-8') as extra_file:
                                extra_data = extra_file.read()
                                buffer_extra_data = base64.b64encode(bytes(extra_data, encoding = 'utf-8'))

                                extras_data.append({
                                    'path': f'{path_extra}',
                                    'code': f'{buffer_extra_data}'
                                })
                        else:
                            logprint.error(f'Extra path {path_extra} is not found and not exists')
            else:
                extras_data = 'no_extras_found'
            
            logprint.info('Generated renderer data')
            logprint.debug(f'buffer_data: {buffer_data} | extras: {extras_data} | manifest: {configure}')
            
            return json_response({
                'message': f'http://server:4444/api/v1/renderer/setup',
                'manifest': {
                    'renderer': {
                        'name': configure['renderer_data']['renderer_name'],
                        'id': configure['renderer_data']['renderer_id'],
                        'author': configure['renderer_data']['author'],
                        'version': configure['renderer_data']['version']
                    }
                },
                'source': {
                    'main': f'{buffer_data}',
                    'extras': extras_data
                }
            })
        except Exception as e:
            logprint.error(f'Got error while generated renderer data: {e}')
            return json_response({'message': 'While generated renderer data script got error. Check your server console to see error.'})
        
    @routes.get('/api/v1/renderer/setup')
    async def api_renderer_setup(request: Request):
        return json_response({'object': f'{setup()}'})
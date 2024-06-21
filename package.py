# Renderer is too difficult than server here...
import base64
import os

from dist.manifest import configure
from src import logprint

try:
    with open('./dist/main.py', 'r', encoding = 'utf-8') as file_data:
        data = file_data.read()
        
    buffer_data = base64.b64encode(bytes(data, encoding = 'utf-8'))
    logprint.info('Main code data encoded')
    
    # NOTE: Checking of extras
    logprint.info('Finding extras on this renderer')
    if configure['extras'] != []:
        logprint.info('This renderer have extras, encoding them too')
        extras_data = []
        
        for cycle_extra in range(0, len(configure['extras'])):
            for path_extra in configure['extras'][cycle_extra]:
                if os.path.exists(path_extra):
                    with open(path_extra, 'r', encoding = 'utf-8') as extra_file:
                        extra_data = extra_file.read()
                        buffer_extra_data = base64.b64encode(bytes(extra_data, encoding = 'utf-8'))

                        extras_data.append({
                            'path': f'{path_extra}',
                            'code': buffer_extra_data
                        })
                        logprint.info(f'Encoded {path_extra}')
                else:
                    logprint.error(f'Extra path {path_extra} is not found and not exists')
    else:
        logprint.info('Extras not found, skipping...')
        extras_data = 'no_extras_found'
        
    logprint.info('Writing encoded data')
    os.system('mkdir package')
    
    code = f'''manifest = {{
    'info': {{'name': '{configure['renderer_data']['renderer_name']}', 'id': '{configure['renderer_data']['renderer_id']}', 'author': '{configure['renderer_data']['author']}', 'version': '{configure['renderer_data']['version']}'}},
    'source_code': {buffer_data},
    'extras': {extras_data}
}}'''
    
    with open('./package/renderer.py', 'a+', encoding = 'utf-8') as package_make:
        package_make.write(code)
        logprint.info('\'./package/renderer.py\' was saved')
        
    with open('./package/README.md', 'a+', encoding = 'utf-8') as readme:
        readme.write('# Renderer\n- ???')
        logprint.info('\'./package/README.md\' was saved')
        
    logprint.info('Wrote encoded data and wrote manifest data')
        
except Exception as e:
    logprint.error(f'Error while packaging renderer: {e}')
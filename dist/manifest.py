__renderer_name__ = 'Name'
__renderer_id__ = 'name'
__author__ = 'You'
__version__ = '1.0'

configure = {
    'workout_file': 'main.py',
    'renderer_data': {
        'renderer_name': __renderer_name__,
        'renderer_id': __renderer_id__,
        'author': __author__,
        'version': __version__
    },
    'extras': [
        {'./dist/lib/test.py'}
    ]
}
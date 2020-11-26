from PyInquirer import prompt
from pprint import pprint

def mainMenu():

    menuOpts = [
        {
            'type': 'list',
            'name': 'Action menu',
            'message': 'Select wanted action',
            'choices': [
                'Change codec',
                'Create mosaic',
                'Streaming',

            ]
        },
        {
            'type': 'input',
            'name': 'video file',
            'message': 'Introduce video file path'
        }
    ]

    return prompt(menuOpts)

def codecMenu():

    menuOpts = [
        {
            'type': 'list',
            'name': 'Codec menu',
            'message': 'Select wanted codec from list',
            'choices': [
                'VP8',
                'VP9',
                'H265',
                'AV1',
            ]
        }
    ]

    return prompt(menuOpts)

def menuIPs():

    menuOpts = [
        {
            'type': 'input',
            'name': 'IP',
            'message': 'Introduce IP for streaming'
        },
        {
            'type': 'input',
            'name': 'port',
            'message': 'Introduce port for streaming'
        }
    ]

    return prompt(menuOpts)

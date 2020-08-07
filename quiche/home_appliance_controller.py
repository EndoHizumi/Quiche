from quiche.adrsirlib import adrsirlib as ir
from quiche.exceptions.exceptions import UnknownTypeError
import requests
import os
import json

command_files_dir = os.path.join(os.path.dirname(__file__), 'commands')


def send(command, name):
    command_file_path = os.path.join(command_files_dir, f'{name}.json')
    with open(command_file_path) as command_json:
        commands = json.load(command_json)
        command_type = commands[name]['type']
        if command_type == 'ir':
            print(f'{name} is type IR')
            ir.send(commands[name][commands])
        elif command_type == 'wi-fi':
            print(f'{name} is type Wi-Fi')
        else:
            raise UnknownTypeError('')

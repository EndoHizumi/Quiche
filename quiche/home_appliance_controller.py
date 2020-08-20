from quiche.adrsir import adrsir as ir
from quiche.exceptions.exceptions import UnknownTypeError
import requests
import os
import json

command_files_dir = os.path.join(os.path.dirname(__file__), 'commands')


def send(command, name):
    command_file_path = os.path.join(command_files_dir, f'{name}.json')
    with open(command_file_path) as command_json:
        commands = json.load(command_json)
        command_type = commands['type']
        if command_type == 'ir':
            ir.trans(commands[command])
            return(f'IR Command {command} send for {name}!')
        elif command_type == 'wi-fi':
            return(f'send to request {command} for {name}!')
        else:
            raise UnknownTypeError('')

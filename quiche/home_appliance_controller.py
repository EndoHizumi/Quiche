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

def show(name):
    command_file_path = os.path.join(command_files_dir, f'{name}.json')
    with open(command_file_path) as command_json:
        commands = json.load(command_json)
        action_lists = {}
        action_lists['name'] = name
        action_lists['commands'] = list(commands.keys())
        action_lists['type'] = commands['type']
    return json.dumps(action_lists)

def read(name, button_no, action):
    """adrsirで記録した赤外線パターンをJSONに保存する

    記録したボタン番号と記憶したリモコンのボタンの名前（テレビなら、音量アップや８チャンネルなど）、操作される機器の名前を指定する

    Args:
        name : 操作される機器の名前（テレビなど。日本語可）
        button_no : ADRSIRの記録したボタンの番号
        action : 記憶させた赤外線パターンの登録名（テレビの電源を入れるなら、wakeなど。日本語可）
    """    


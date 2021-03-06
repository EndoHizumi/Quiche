from quiche.adrsir import adrsir as ir
from quiche.exceptions.exceptions import UnknownTypeError
import requests
import os
import json
from typing import Dict, List

command_files_dir = os.path.join(os.path.dirname(__file__), 'commands')


def send(command: str, name: str) -> str:
    """入力された登録名とコマンド名に紐づいた赤外線パターンを送信する

    Args:
        command: 登録した赤外線パターンの名前
        name: 登録した家電の名前

    Raises:
        UnknownTypeError: 指定された家電のtypeの値がirかwi-fiのどちらでもない場合に発生する
    """

    command_file_path = os.path.join(command_files_dir, f'{name}.json')
    with open(command_file_path) as command_json_file:
        command_dict = json.load(command_json_file)
        command_type = command_dict['type']
        if command_type == 'ir':
            ir.trans(command_dict[command])
            return(f'IR Command {command} send for {name}!')
        elif command_type == 'wi-fi':
            return(f'send to request {command} for {name}!')
        else:
            raise UnknownTypeError('')


def show(name: str) -> Dict[str, str]:
    """登録されたコマンド名一覧を返す

    Args:
        name: 登録した家電の名前
    """

    command_file_path = os.path.join(command_files_dir, f'{name}.json')
    with open(command_file_path) as command_json_file:
        command_dict = json.load(command_json_file)
        command_lists = {}
        command_lists['name'] = name
        command_lists['command_dict'] = list(command_dict.keys())[1:]
        command_lists['type'] = command_dict['type']
    return command_lists


def read(name: str, button_no: list, command: list) -> List[str]:
    """adrsirで記録した赤外線パターンをJSONに保存する

    記録したボタン番号と記憶したリモコンのボタンの名前（テレビなら、音量アップや８チャンネルなど）、操作される機器の名前を指定する

    Args:
        name : 操作される機器の名前（テレビなど。日本語可）
        button_no : ADRSIRの記録したボタンの番号。
        command : 記憶させた赤外線パターンの登録名（テレビの電源を入れるなら、wakeなど。日本語可）
    """

    pattern_list = {}
    result = []
    command_file_path = os.path.join(command_files_dir, f'{name}.json')
    if (os.path.exists(command_file_path)):
        with open(command_file_path) as f:
            pattern_list = json.load(f)
    else:
        pattern_list['type'] = 'ir'

    for button, command_name in zip(button_no, command):
        pattern_list[command_name] = ir.read(button)
        result += [f'registered {command_name} of {name}']

    with open(command_file_path, 'w') as command_json_file:
        json.dump(pattern_list, command_json_file)

    return result

from flask import Blueprint

import commands


commands_index = Blueprint('commands_index', __name__)

@commands_index.route('/')
def command_test():
    print('Test...')
    return "", 200

@commands_index.route('/kick_process')
def kick_process():
    print('[start] kick process...')
    commands.kick_process()
    print('[end] kick process...')
    return "", 200

@commands_index.route('/get_status')
def get_status():
    print('[start] get status...')
    commands.get_status()
    print('[end] get status...')
    return "", 200

@commands_index.route('/stop_process')
def stop_process():
    print('[start] stop process...')
    commands.exit_process()
    print('[end] stop process...')
    return "", 200
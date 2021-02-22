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

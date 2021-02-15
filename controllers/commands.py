from flask import Blueprint

from commands import sample_process


commands = Blueprint('commands', __name__)

@commands.route('/')
def command_test():
    print('Test...')
    return "", 200

@commands.route('/kick_process_sample')
def kick_process_sample():
    print('[start] kick process...')
    sample_process()
    print('[end] kick process...')
    return "", 200

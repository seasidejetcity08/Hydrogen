from flask import Blueprint

commands = Blueprint('commands', __name__)

@commands.route('/')
def command_test():
    print('Test...')
    return "", 200

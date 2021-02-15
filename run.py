from flask import Flask
from controllers import commands

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(commands)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    debug = True
    use_reloader = False
    use_debugger = True
    app.run(host=host, port=port, debug=debug, use_reloader=use_reloader, use_debugger=use_debugger)

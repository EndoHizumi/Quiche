from os import abort
from flask import Flask
import quiche.home_appliance_controller as quiche

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/', methods={'GET'})
def hello():
    return "hello"


@app.route('/<command>/<name>', methods=['GET'])
def send_command(command, name):
    try:
        quiche.send(command, name)
        return "OK"
    except FileNotFoundError:
        return abort(404)
    except KeyError:
        return abort(400)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)

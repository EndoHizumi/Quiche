from os import abort
from flask import Flask
import quiche.home_appliance_controller as quiche

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/', methods={'GET'})
def hello():
    return "hello"

@app.route('/signals/<name>/<action>', methods=['PUT'])
def add_command(button_no, name, action):
    pass

@app.route('/signals/<name>/<action>', methods=['POST'])
def send_command(name, action):
    try:
        result = quiche.send(action, name)
        return result
    except FileNotFoundError:
        return abort(404)
    except KeyError:
        return abort(400)

@app.route('/signals/<name>', methods=['GET'])
def list_command(name):
    try:
        result = quiche.show(name)
        return result
    except FileNotFoundError:
        return abort(404)
    except KeyError:
        return abort(400)

@app.route('/appliances')
def list_appliance():
    pass

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080, threaded=True)

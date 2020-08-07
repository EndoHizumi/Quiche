from os import abort
from flask import Flask, request
import home_appliance_controller

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/', methods={'GET'})
def hello():
    return "hello"

@app.route('/<command>/<name?', methods=['GET'])
def send_command(command, name):
    try:
        home_appliance_controller.send(command, name)
    except FileNotFoundError:
        abort(404)
    except KeyError:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)

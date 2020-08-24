import os
from flask import Flask, request, jsonify
import quiche.home_appliance_controller as quiche

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/', methods={'GET'})
def hello():
    return "hello"


@app.route('/signals/<name>', methods=['PUT'])
def add_command(name):
    button_no_list = request.json['button_no_list']
    action_names = request.json['action_names']
    result = quiche.read(name, button_no_list, action_names)
    return jsonify(result)


@app.route('/signals/<name>/<action>', methods=['POST'])
def send_command(name, action):
    try:
        result = quiche.send(action, name)
        return jsonify(result)
    except FileNotFoundError:
        return jsonify({'message': 'Not Found'}), 404
    except KeyError:
        return jsonify({'message': 'Bad Request'}), 400


@app.route('/signals/<name>', methods=['GET'])
def list_command(name):
    try:
        result = quiche.show(name)
        return jsonify(result)
    except FileNotFoundError:
        return jsonify({'message': 'Not Found'}), 404
    except KeyError:
        return jsonify({'message': 'Bad Request'}), 400


@app.route('/appliances')
def list_appliance():
    appliances_file_path = os.path.join(os.path.dirname(__file__), "quiche/commands")
    print(appliances_file_path)
    result = [os.path.splitext(filename)[0] for filename in os.listdir(appliances_file_path)]
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080, threaded=True)

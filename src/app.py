from flask import Flask, request


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/', methods={'GET'})
def hello():
    return "hello"

def 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)

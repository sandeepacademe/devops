from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

about =  {
            "version" : "0.1",
            "name"    : "my-web-server-beta:1.0.1"
        }

contact = '{"contact": "developer@mywebserver.test"}'

users = []

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, my-web-server-beta!"

@app.route('/about', methods=['GET'])
def about_fn():
    return jsonify({'about' : about})

@app.route('/contact', methods=['GET'])
def contact_fn():
    json_object = json.loads(contact)
    return (json.dumps(json_object, indent = 3))

if __name__ == "__main__":
    app.run(debug=True)

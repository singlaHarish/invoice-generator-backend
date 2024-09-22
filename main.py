from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route('/hello')
def hello_world():
    return 'Hello, World!!!'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

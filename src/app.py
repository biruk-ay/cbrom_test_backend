from flask import Flask, request
from utils.usage import Usage
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ["GET"])
def hello():
    a = Usage()
    return a.get_all_info()

if __name__ == '__main__':
    app.run()

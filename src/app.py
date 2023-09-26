from flask import Flask, request
from utils.usage import Usage
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ["GET"])
def hello():
    a = Usage()
    return a.get_all_info()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

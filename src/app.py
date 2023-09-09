from flask import Flask
from utils.usage import Usage

app = Flask(__name__)

@app.route('/')
def hello():
    a = Usage()
    return a.get_all_info()

if __name__ == '__main__':
    app.run()

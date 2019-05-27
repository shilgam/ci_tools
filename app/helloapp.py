import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0')

"""
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +    Single hello world using flask                        +
    +    Installing flask: pip3 install flask (terminal)       +
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)

# FLASK_APP=hello.py flask run

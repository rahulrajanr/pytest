import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!webhook works build 13"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return contents

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

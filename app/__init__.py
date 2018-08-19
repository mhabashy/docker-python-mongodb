"""
DOCKER + PYTHON + MONGODB Starter by Michael Habashy
"""

from flask import Flask, json

from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('mongodb://{}:{}@mongo:27017'.format('root', 'example'))


@app.route("/")
def enter():
    return "docker + python + mongodb"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
    print('APP LOADED!')
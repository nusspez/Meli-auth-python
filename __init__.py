from flask import Flask

app = Flask(__name__)
PORT = 5000
DEBUG = False

from app import routes

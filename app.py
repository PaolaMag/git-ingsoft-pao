
from flask import Flask

from flask import request

 

app = Flask(__name__)

 

@app.route('/')

def hello():

 

    return '<h1>Hello, World! desde la branch  Feature2 por Margiory</h1>'


from flask import Flask

from flask import request

 

app = Flask(__name__)

 

@app.route('/')

def hello():

 



 return '<h1>Hello, World! desde Feature2 a Feature3</h1>'


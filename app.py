import json
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/webhooks',  methods=['POST'])
def webhooks():
    data = json.load(request.data)
    
    print(data)
           

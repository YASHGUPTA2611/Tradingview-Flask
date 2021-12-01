import json
from action import *
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/webhooks',  methods=['POST'])
def webhook():
    
    print("HERE WE WILL GET PARAMS OF THE ALERT FROM TRADINGVIEW")
    data = json.loads(request.data)
    print(data['ticker'])
    print(data['bar'])

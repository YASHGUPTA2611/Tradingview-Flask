import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>This is my first trading bot</h1>"


@app.route('/webhook', methods=['POST'])
def webhook():

    data = json.loads(request.data)
    
    print(data['ticker'])
    print(data['exchange'])
   

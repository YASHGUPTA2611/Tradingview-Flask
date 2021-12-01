import json
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/webhooks',  methods=['POST'])
def webhook():
    if request.method=='POST':
        data = parse_webhook(request.get_data(as_text=True))
        Print("Alert Received")
           

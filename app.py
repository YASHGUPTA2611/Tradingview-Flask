import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>This is my first trading bot</h1>"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    webhook_message = jsonify(request.json)

    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
   

import json
import request
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>This is my first trading bot</h1>"


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
   

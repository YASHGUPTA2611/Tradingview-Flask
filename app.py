
from flask import Flask, request,abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/webhooks', methods = ['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)






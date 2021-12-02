import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>This is my first trading bot</h1>"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    webhook_message = jsonify(request.json)
    
    side = data['strategy']['order_action'].upper()
    quantity = data['strategy']['order_contracts']
    order_response = order(side, quantity, "DOGEUSD")

    if order_response:
        return {
            "code": "success",
            "message": "order executed"
        }
    else:
        print("order failed")

        return {
            "code": "error",
            "message": "order failed"
        }

if __name__ == '__main__':
    app.run(debug=True)
   

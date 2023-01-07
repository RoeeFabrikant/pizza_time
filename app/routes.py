from flask import Flask, request, jsonify
from flask import current_app as app
from app.src.order import pizza_order

@app.post('/order')
def new_order():
  pizza_type = request.form.get('pizza_type')
  size = request.form.get('size')
  amount = request.form.get('amount')

  return pizza_order(pizza_type, size, amount)

@app.get('/ping')
def ping():
  return jsonify({'message': 'Pong!',
                  'return_code': 200}), 200

@app.get('/health')
def health_check():
  return jsonify({'message': 'App is healthy, order your pizza!',
                  'return_code': 200}), 200

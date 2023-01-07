
from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.INFO, format=f'%(asctime)s [%(levelname)s] : %(message)s')

pizza_sizes = ['personal', 'fammily']
pizza_flavors = ['napolitana','salami', 'pork', 'pinapple']

def pizza_order(pizza_type, size, amount):
  if not all([pizza_type, size, amount]):
    logging.warning('User entered an order with missing parameters')
    message = 'Please fill out all form fields'
    order_status = 'Failed'
    return_code = 400
  elif not amount.isdigit():
    logging.warning('User entered an order with amount typo')
    message = 'Amount must be a number'
    order_status = 'Failed'
    return_code = 400
  elif size not in pizza_sizes:
    logging.warning('User entered an order with wrong pizza size')
    message = f"The pizza size does not exist. available sizes: {'/'.join(pizza_sizes)}"
    order_status = 'Failed'
    return_code = 400
  elif pizza_type not in pizza_flavors:
    logging.warning('User entered an order with wrong pizza type')
    message = f"The pizza flavor does not exist. available flavors: {'/'.join(pizza_flavors)}"
    order_status = 'Failed'
    return_code = 400
  else:
    logging.info('New order received')
    message = 'Order placed successfully! Thanks for your order!'
    order_status = 'Complete'
    return_code = 200

  return jsonify({'order_status': order_status,
                  'message': message,
                  'return_code': return_code}), return_code

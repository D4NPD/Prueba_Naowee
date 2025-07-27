from flask import request, Blueprint, jsonify
from auth import token_required, require_role
from models import createOrder, getAllOrders, getOrderDetails, getOrderbyUserId

order_bp = Blueprint('order', __name__)

@order_bp.route('/create_order', methods=['POST'])
@token_required
def create_order():
  data = request.get_json()
  user_id = data.get('user_id')
  response = createOrder(user_id)
  return jsonify(response), 201 if 'order_id' in response else 400

@order_bp.route('/get_order/<user_id>', methods=['GET'])
@token_required
def get_order_by_user(user_id):
  response = getOrderbyUserId(user_id)
  return jsonify(response)

@order_bp.route('/get_order_details/<order_id>', methods=['GET'])
@token_required
def get_order_details(order_id):
  response = getOrderDetails(order_id)
  return jsonify(response), 200 if 'error' not in response else 404

@order_bp.route('/get_all_orders', methods=['GET'])
@require_role('admin')
def get_all_orders():
  response = getAllOrders()
  return jsonify(response)
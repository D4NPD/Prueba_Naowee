from flask import request, jsonify, Blueprint
from auth import token_required, require_role
from models import addProductToCart, deleteProductFromCart, emptyCart, getCartByUserId, updateAmountInCart

shopping_cart_bp = Blueprint('shopping_cart', __name__)

@shopping_cart_bp.route('/cart/<user_id>', methods=['GET'])
@token_required
def get_cart_by_userId(user_id):
  try: 
    cart_items = getCartByUserId(user_id)
    if not cart_items:
      return jsonify({'message': 'Cart is empty'}), 404
    return jsonify(cart_items), 200
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@shopping_cart_bp.route('/cart/add', methods=['POST'])
@token_required
def add_product_to_cart():
  try:
    data = request.get_json()
    response = addProductToCart(data['user_id'], data['product_id'], data['amount'])
    return jsonify(response), 200
  except Exception as e:  
    return jsonify({'error': str(e)}), 500
  
@shopping_cart_bp.route('/cart/update/<cart_product_id>', methods=['PUT'])
@token_required
def update_cart_product(cart_product_id):
  try:
    data = request.get_json()
    if not data or 'amount' not in data:
      return jsonify({'error': 'Amount is required'}), 400
    response = updateAmountInCart(cart_product_id, data['amount'])
    if not response:
      return jsonify({'error': 'Cart product not found'}), 404
    return jsonify(response), 200
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@shopping_cart_bp.route('/cart/delete/<cart_product_id>', methods=['DELETE'])
@token_required
def delete_cart_product(cart_product_id):
  try:
    deleted = deleteProductFromCart(cart_product_id)
    if deleted:
      return jsonify({'message': 'Product removed from cart successfully'}), 200
    else:
      return jsonify({'error': 'Cart product not found'}), 404
  except Exception as e:
    return jsonify({'error': str(e)}), 500
  
@shopping_cart_bp.route('/cart/empty/<user_id>', methods=['DELETE'])
@token_required
def empty_cart(user_id):
  try:
    emptied = emptyCart(user_id)
    if emptied:
      return jsonify({'message': 'Cart emptied successfully'}), 200
    else:
      return jsonify({'error': 'No cart found for this user'}), 404
  except Exception as e:
    return jsonify({'error': str(e)}), 500
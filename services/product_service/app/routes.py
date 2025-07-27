from flask import Blueprint, request, jsonify
from auth import token_required, require_role
from models import createProduct, deleteProduct, getProducts, getProductById, updateProduct

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
@token_required
def get_products():
  try:
    products = getProducts()
    return jsonify(products), 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500
  
@product_bp.route('/products/<id>', methods=['GET'])
@token_required
def get_product(id):
    try:
        product = getProductById(id)
        if product:
            return jsonify(product), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@product_bp.route('/products', methods=['POST'])
@require_role('admin')
def create_product():
    try:
        product = request.json
        if not product or not all(key in product for key in ('name','unit_price')):
            return jsonify({"error": "Product required name and price"}), 400
        
        product_id = createProduct(product)
        return jsonify({"product_id": product_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@product_bp.route('/products/<id>', methods=['PUT'])
@require_role('admin')
def update_product(id):
    try:
        product = request.json
        if not product or not all(key in product for key in ('name','unit_price')):
            return jsonify({"error": "Product required name and price"}), 400
        
        updated = updateProduct(id, product)
        if updated:
            return jsonify({"message": "Product updated successfully"}), 200
        else:
            return jsonify({"error": "Product not found or no changes made"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@product_bp.route('/products/<id>', methods=['DELETE'])
@require_role('admin')
def delete_product(id):
    try:
        deleted = deleteProduct(id)
        if deleted:
            return jsonify({"message": "Product deleted successfully"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
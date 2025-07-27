from flask import Blueprint, jsonify, request
from models import create_Newcategory, delete_Onecategory, get_Allcategories, get_Onecategory, update_Onecategory
from auth import require_role
category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
@require_role('admin')  # Assuming you want to restrict this endpoint to admin users
def get_categories():
    try:
        categories = get_Allcategories()  # Should return a list/dict, not a Response
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@category_bp.route('/categories/<id>', methods=['GET'])
@require_role('admin')  # Assuming you want to restrict this endpoint to admin users
def get_category(id):
    try:
        category = get_Onecategory(id)  # Should return a single category or None
        if category:
            return jsonify(category), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@category_bp.route('/categories', methods=['POST'])
@require_role('admin')  # Assuming you want to restrict this endpoint to admin users
def create_category():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        
        if not name or not description:
            return jsonify({"error": "Name and description are required"}), 400
        
        category_id = create_Newcategory(name, description)  # Should return the new category ID
        return jsonify({"category_id": category_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@category_bp.route('/categories/<id>', methods=['PUT'])
@require_role('admin')  # Assuming you want to restrict this endpoint to admin users
def update_category(id):
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        
        if not name or not description:
            return jsonify({"error": "Name and description are required"}), 400
        
        updatedStatus = update_Onecategory(id, name, description)  # Should return True/False
        if updatedStatus:
            return jsonify({"message": "Category updated successfully"}), 200
        else:
            return jsonify({"error": "Category not found or update failed"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@category_bp.route('/categories/<id>', methods=['DELETE'])
@require_role('admin')  # Assuming you want to restrict this endpoint to admin users
def delete_category(id):
    try:
        deletedStatus = delete_Onecategory(id)  # Should return True/False
        if deletedStatus: 
            return jsonify({"message": "Category deleted successfully"}), 200
        else:
            return jsonify({"error": "Category not found or delete failed"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
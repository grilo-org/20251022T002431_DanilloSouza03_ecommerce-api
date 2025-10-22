from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.models import db, login_manager, User, Product, CartItem

api_bp = Blueprint('api', __name__)

@api_bp.route('/register',  methods=["POST"])
def fazer_cadastro():
    data = request.get_json() or {}

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    try:
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Database error", "details": str(e)}), 500

@api_bp.route('/login', methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401

    if check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

@api_bp.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout sucessfully!"})

@api_bp.route('/api/products/add', methods=["POST"])
@login_required
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully!"})
    return jsonify({"message": "Invalid product data!"}), 400

@api_bp.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"})
    return jsonify({"message": "Product not found"}), 404

@api_bp.route('/api/products/<int:product_id>', methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name, 
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "Product not found"}), 404

@api_bp.route('/api/update/<int:product_id>', methods=["PUT"])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found!"}), 404
    
    data = request.json
    if 'name' in data:
        product.name = data['name']
    
    if 'price' in data:
        product.price = data['price']
    
    if 'description' in data:
        product.description = data['description']

    db.session.commit()    
    
    return jsonify({"message": "Product modified successfully!"})

@api_bp.route('/api/products', methods=["GET"])
def get_products():
    products = Product.query.all()
    
    list_products = []
    for product in products:
        data_product = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        }
        list_products.append(data_product)

    return jsonify(list_products)

@api_bp.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    user = User.query.get(int(current_user.id))
    product = Product.query.get(product_id)

    if user and product:
        cart_item = CartItem(user_id=user.id, product_id=product.id)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({"message": "Item added to the cart successfully!"})
    return jsonify({"message": "Failed to add the cart!"}), 400

@api_bp.route('/api/cart/remove/<int:product_id>', methods=["DELETE"])
@login_required
def remove_from_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Item removed from the cart successfully!"})
    return jsonify({"message": "Failed to remove item from the cart!"}), 400

@api_bp.route('/api/cart', methods=['GET'])
@login_required
def view_cart():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    list_cart = []
    for item in cart_items:
        product = Product.query.get(item.product_id)
        list_cart.append({"id": item.id, "user_id": item.user_id, "product_id": item.product_id, "product_name": product.name, "product_price": product.price})
    return jsonify(list_cart)

@api_bp.route('/api/cart/checkout', methods=["POST"])
@login_required
def checkout():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    for item in cart_items:
        db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Checkout successfully. Cart has been cleared."})
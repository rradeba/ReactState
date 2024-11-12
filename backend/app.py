from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:843RnR$$@localhost/fitness_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app) 

# Schemas
class CustomerSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ("name", "email", "phone")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

class CustomerAccountSchema(ma.Schema):
    user_name = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        fields = ("user_name", "password")

account_schema = CustomerAccountSchema()
accounts_schema = CustomerAccountSchema(many=True)

class ProductSchema(ma.Schema):
    vin = fields.String(required=True)
    name = fields.String(required=True)
    price = fields.String(required=True)

    class Meta:
        fields = ("vin", "name", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class OrderSchema(ma.Schema):
    number = fields.String(required=True)
    shipping_address = fields.String(required=True)
    payment_method = fields.String(required=True)

    class Meta:
        fields = ("number", "shipping_address", "payment_method")

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Models
class Customer(db.Model):
    __tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)

class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(255), nullable=False)
    shipping_address = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(255), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    vin = db.Column(db.Integer, db.ForeignKey('product.vin'))

class Product(db.Model):
    __tablename__ = 'product'
    vin = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)

class CustomerAccount(db.Model):
    __tablename__ = 'customer_account'
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))

# POST method for adding customer to the database
@app.route('/customer', methods=['POST'])
def add_customer():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_customer = Customer(
        name=customer_data['name'],
        email=customer_data['email'],
        phone=customer_data['phone']
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer added successfully"}), 201

# POST method for adding customer account to the database
@app.route('/customer_account', methods=['POST'])
def add_customer_account():
    try:
        customer_account_data = account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_customer_account = CustomerAccount(
        user_name=customer_account_data['user_name'],
        password=customer_account_data['password'],
        customer_id_fk=request.json['customer_id']
    )
    db.session.add(new_customer_account)
    db.session.commit()
    return jsonify({"message": "Customer account added successfully"}), 201

# POST method for adding product to the database
@app.route('/product', methods=['POST'])
def add_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_product = Product(
        vin=product_data['vin'],
        name=product_data['name'],
        price=product_data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

# POST method for adding order to the database
@app.route('/order', methods=['POST'])
def add_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_order = Order(
        number=order_data['number'],
        shipping_address=order_data['shipping_address'],
        payment_method=order_data['payment_method'],
        customer_id=request.json['customer_id'],
        vin=request.json['vin']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order added successfully"}), 201

# GET method for customer
@app.route('/customer/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return customer_schema.jsonify(customer)

# GET method for product
@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

# GET method for all products
@app.route('/account', methods=['GET'])
def get_account():
    products = CustomerAccount.query.all()
    return account_schema.jsonify(products)

# GET method for order
@app.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return order_schema.jsonify(order)

# GET method for all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return orders_schema.jsonify(orders)

# PUT method for updating a customer
@app.route('/customer/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    customer.name = customer_data['name']
    customer.email = customer_data['email']
    customer.phone = customer_data['phone']
    db.session.commit()
    return jsonify({"message": "Customer updated successfully"}), 200

# PUT method for updating a customer account
@app.route('/customer_account/<int:id>', methods=['PUT'])
def update_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    try:
        account_data = account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    account.user_name = account_data['user_name']
    account.password = account_data['password']
    db.session.commit()
    return jsonify({"message": "Customer account updated successfully"}), 200

# PUT method for updating a product
@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    product.vin = product_data['vin']
    product.name = product_data['name']
    product.price = product_data['price']
    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200

# PUT method for updating an order
@app.route('/order/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    order.number = order_data['number']
    order.shipping_address = order_data['shipping_address']
    order.payment_method = order_data['payment_method']
    db.session.commit()
    return jsonify({"message": "Order updated successfully"}), 200

# DELETE method for deleting a customer
@app.route('/customer/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully"}), 200

# DELETE method for deleting a customer account
@app.route('/customer_account/<int:id>', methods=['DELETE'])
def delete_account(id):
    account = CustomerAccount.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    return jsonify({"message": "Customer account deleted successfully"}), 200

# DELETE method for deleting a product
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200

@app.route('/order/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
















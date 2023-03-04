from flask import Flask, request, jsonify
from models import db, User

app = Flask(__name__)

# sign up
@app.route('/users', methods=['POST'])
def signup():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json('email')
    password = request.json.get('password')

    if User.query.filter_by(username=username).first():
        return "Username already exists", 409

    if User.query.filter_by(email=email).first():
        return "Email already exists", 409

    index = email.find('@usc.edu')
    if index == -1:
        return "Email is not a USC email", 409
    
    user = User(username=username, email=email, password=password)
    db.sesssion.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201

# login
@app.route('/users/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).first()
    if user is None:
        return "User does not exist", 404

    if user.password != password:
        return "Incorrect password", 401

    return jsonify(user.serialize()), 200
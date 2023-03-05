from flask import Flask, jsonify, request, session, redirect
# from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }

    # Encrypt the password
    # user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    # check to make sure email is USC email
    index = user['email'].find('@usc.edu')
    if index == -1:
      return jsonify({ "error": "Email is not a USC email" }), 400


    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  #f
  def signout(self):
    session.clear()
    return redirect('/')
  
  def loginEmail(self):

    email = request.form.get('email')
    password = request.form.get('password')

    user = db.users.find_one({
      "email": request.form.get('email')
    })
    if user is none:
      return "User does not exist", 404

    if user.password != password:
      return "Incorrect password", 401
    
    if user and user['password'] == password:
      return self.start_session(user)
  
    # return jsonify({ "error": "Invalid login credentials" }), 401

  def loginGoogle(self):
    authorization
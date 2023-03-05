from flask import Flask
from app import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/products', methods=['GET', 'POST'])
def product_handler():
  if request.method == 'GET'
    # Handle GET request to retrieve products
        return 'Retrieving products...'
    elif request.method == 'POST':
        # Handle POST request to create a new product
        return 'Creating a new product...'




if __name__ == '__main__':
    app.run(port=3000)
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/users', methods=['GET', 'POST'])
def user_handler():
    if request.method == 'GET':
        # Handle GET request to retrieve users
        return 'Retrieving users...'
    elif request.method == 'POST':
        # Handle POST request to create a new user
        return 'Creating a new user...'

@app.route('/products', methods=['GET', 'POST'])
def product_handler():
    if request.method == 'GET':
        # Handle GET request to retrieve products
        return 'Retrieving products...'
    elif request.method == 'POST':
        # Handle POST request to create a new product
        return 'Creating a new product...'




if __name__ == '__main__':
    app.run(port=3000)
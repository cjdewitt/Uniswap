from venmo_api import Client



@app.route('/venmo', methods=['POST'])
def venmoLogin():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    # Get your access token. You will need to complete the 2FA process
    access_token = Client.get_access_token(username=email,
                                        password=password)
    venmo = Client(access_token=access_token)


def venmoSend():
    # Send a payment to a user
    payment = venmo.payment.request_money(1.00, 'Test', 'user-id')

    # Send a payment to a user's phone number
    payment = venmo.payment.request_money(1.00, 'Test', phone='1234567890')

    # Send a payment to a user's email
    payment = venmo.payment.request_money(1.00, 'Test')



def venmoRequest():
    # Request money from a user
    payment = venmo.payment.request_money(1.00, 'Test', 'user-id')

    # Request money from a user's phone number
    payment = venmo.payment.request_money(1.00, 'Test', phone='1234567890')

    # Request money from a user's email
    payment = venmo.payment.request_money(1.00, 'Test',
from flask import request
from model.models import Auth


def basic_auth_required(func):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_basic_auth(auth.username, auth.password):
            return authenticate()
        return func(*args, **kwargs)
    decorated.__name__ = func.__name__
    return decorated


def check_basic_auth(username, password):
    # Perform your authentication logic here
    # You can check the credentials against a database, file, or any other method
    # Return True if the credentials are valid, False otherwise
    # Example:
    auth_response = Auth.query.filter_by(username=username).first_or_404()

    return username == auth_response.username and password == auth_response.password


def authenticate():
    response = {
        "Message": "Authentication Required"
    }

    return response

from flask import Blueprint
from flask_restplus import Api, Resource

auth = Blueprint('auth_api', __name__)

authapi = Api(auth)

@authapi.route('/login/')
class UserLogin(Resource):
    def get(self):
        return "Hello, User"

@authapi.route('/logout/')
class UserLogout(Resource):
    def get(self):
        return "Goodbye, User"

@authapi.route('/password/')
class UserPassword(Resource):
    def post(self):
        return "Change Password"
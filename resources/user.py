import sqlite3 #this gives the ability to inteRACT with sqlite
from flask_restful import Resource, reqparse
from models.user import UserModel

#User class must not be same as resource we use to sign up
#could make a flask endpoint instead of making new resource
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field must not be blank")
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field shall not be blank")

    def post(self):
        data=UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "user with that name already exists"}

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

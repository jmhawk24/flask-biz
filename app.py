from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db
#these imports are important for the app firing up and for SQLAlchemy knowing what to create tables for

#resources usually mapped into database tables as well
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #doesn't have to be sqlite, but sqlalchemy just works
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity) #initialize JWT object needs functions from security.py
#JWT creates new endpoint /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(UserRegister, '/register')

api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__': #this prevents the app from running when imported
    db.init_app(app)
    app.run(port=5000, debug=True)

#need to handle exceptions because JSON still needs to be valid
#201 message means something is created
#202 code is when something is accepted but not yet created. good for async
#in get_json(force=true) means you do not need content-type header. it will force it into JSON
#this will cause us to always process the request even with the wrong datatype
#Silent=True means it does not give any errors, just stays silent
#filter function returns a filter object. call methods on those objects to use
#list(filterObject) returns a list
#next(filterObject) returns first item found by filter function
#next(filterObject, defaultValue)
#use it like next(filterObject, None) to prevent errors

#400 is Bad Request
#JWT is JSON Web Token - it obfuscates data (encode)
#they send username and password, we send them a JWT so we know they have authenticated
#Header Authorization: JWT <JWT Token>
#remember that we need @jwt_required for auth purposes
#global <variable> to tell the program we are using a variable from outside a method
#keyerror means we are trying to access a key that is not there

#sqlite does not enforce table restrictions -- so we can make a foreign id point to something that doesn't exist
#e.g. store_id = 1 even though that store doesn't exist

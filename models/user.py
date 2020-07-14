import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) #these variables must match attributes
    #if they don't match it won't be stored or read in database
    username = db.Column(db.String(80)) #number passed in limits size
    password = db.Column(db.String(80))

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod #this gets us to use the current class rather than hard-coding User class
    def find_by_id(cls, _id): #use _id because it is a built in python 'method'
        return cls.query.filter_by(id=_id).first()

#this is an API (not a rest api but it is an api)
#it exposes two endpoints - find_by_id and find_by_username
#they are an interface for other parts of program to interact with user thing
#as long as methods return the same thing they can be changed

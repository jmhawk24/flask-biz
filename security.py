from werkzeug.security import safe_str_cmp #this compares strings
from resources.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username) #if username_mapping finds nothing, we return None
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

#we do this so we don't have to iterate over the list every time.
#two functions - one authenticates user
# i think this might automatically set up an auth endpoint
#no - it gets passed into the JWT instance in app.py

from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
	user = UserModel.find_by_username(username)                   # given the username and password check if user exists
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	user_id = payload['identity']                            # from the payload take the id the validate
	return UserModel.find_by_id(user_id)
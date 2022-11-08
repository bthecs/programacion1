from .. import jwt
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps


#Restriccion de acceso a los usuarios que no esten autenticados solamente acceden admins
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        jwt_data = get_jwt()
        if jwt_data['rol'] == 'admin':
            return fn(*args, **kwargs)
        return jsonify({'message': 'Admin access required'}), 403
    return wrapper


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id



#Atributos que se guardaran dentro del Token
@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    print(user)
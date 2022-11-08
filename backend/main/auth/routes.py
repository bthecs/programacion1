from cmath import pi
from flask import request, jsonify, Blueprint
from .. import db
from main.models import UserModel
from flask_jwt_extended import create_access_token

#Blueprint para el acceso a los metodos para autenticar
auth = Blueprint('auth', __name__, url_prefix='/auth')



#Método de logueo
@auth.route('/login', methods=['POST'])
def login():

    #Busca al usuario en la db por mail
    user = db.session.query(UserModel).filter(
        UserModel.email == request.get_json().get("email")).first_or_404()
    # print(user.password)
    # print(user.validate_pass(request.get_json().get("password")))
    #Valida la contraseña
    if user.validate_pass(request.get_json().get("password")):
        #Genera un nuevo token
        #Pasa el objeto professor como identidad
        access_token = create_access_token(identity=user)
        #Devolver valores y token
        data = {
            'id': user.id,
            'email': user.email,
            'access_token': access_token
        }

        return data, 200
    else:
        return 'Incorrect password', 401

from flask import request, jsonify, Blueprint
from .. import db
from main.models import UserModel
from flask_jwt_extended import create_access_token

#Blueprint para el acceso a los metodos para autenticar
auth = Blueprint('auth', __name__, url_prefix='/auth')


#Metodo para logear
@auth.route('/login', methods=['POST'])
def login():
    #Obtenemos los datos del usuario
    user = db.session.query(UserModel).filter(UserModel.email == request.json['email']).first_or_404()
    #Validar la contraseña
    if user.validate_pass(request.json['password']):
        #Generamos el token
        access_token = create_access_token(identity=user)
        #Devolvemos los valores
        data = {
            'id': str(user.id),
            'email': user.email,
            'access_token': access_token
        }
        return data, 200
    else:
        return 'Incorrect password', 401
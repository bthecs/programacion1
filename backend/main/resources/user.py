from flask_restful import Resource
from flask import request


#Test Dictionary
USERS = {
    1: {'firstname': 'Lautaro', 'lastname': 'Gimenez'},
    2: {'firstname': 'Pedro', 'lastname': 'Marco'}
}

#Poem resources
class User(Resource):
    
    def get(self, id):
        
        if int(id) in USERS:
            
            return USERS[int(id)]
        
        return '', 404
    
    def put(self, id):
        if int(id) in USERS:
            professor = USERS[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            professor.update(data)
            return professor, 201
        return '', 404

    
    def delete(self, id):
        
        if int(id) in USERS:
            
            del USERS[int(id)]
            return '', 204
        
        return '', 404

class Users(Resource):
    
    def get(self):
        return USERS
    
    def post(self):
        
        user = request.get_json()
        id = int(max(USERS.keys())) + 1
        USERS[id] = user
        return USERS[id], 201
    
        
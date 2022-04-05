from flask_restful import Resource
from flask import request


#Test Dictionary
QUALIFY = {
    1: {'Qualify':'4.5','Hola': 'chau'},
    2: {'Qualify':'4.5','Hola': 'chau'}
}

#Poem resources
class Qualify(Resource):
    
    def get(self, id):
        
        if int(id) in QUALIFY:
            
            return QUALIFY[int(id)]
        
        return '', 404
    
    def put(self, id):
        if int(id) in QUALIFY:
            qualification = QUALIFY[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            qualification.update(data)
            return qualification, 201
        return '', 404
    
    
    def delete(self, id):
        
        if int(id) in QUALIFY:
            
            del QUALIFY[int(id)]
            return '', 204
        
        return '', 404
    
    

class Qualifications(Resource):
    
    def get(self):
        return QUALIFY
    
    def post(self):
        
        qualification = request.get_json()
        id = int(max(QUALIFY.keys())) + 1
        QUALIFY[id] = qualification
        return QUALIFY[id], 201
    
        
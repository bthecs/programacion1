from flask_restful import Resource
from flask import request


#Test Dictionary
POEMS = {
    1: {'title': 'Lautaro', 'description': 'Gimenez'},
    2: {'title': 'Pedro', 'description': 'Marco'}
}

#Poem resources
class Poem(Resource):
    
    def get(self, id):
        
        if int(id) in POEMS:
            
            return POEMS[int(id)]
        
        return '', 404
    
    def put(self, id):
        if int(id) in POEMS:
            professor = POEMS[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            professor.update(data)
            return professor, 201
        return '', 404

    
    def delete(self, id):
        
        if int(id) in POEMS:
            
            del POEMS[int(id)]
            return '', 204
        
        return '', 404

class Poems(Resource):
    
    def get(self):
        return POEMS
    
    def post(self):
        
        poem = request.get_json()
        id = int(max(POEMS.keys())) + 1
        POEMS[id] = poem
        return POEMS[id], 201
    
        
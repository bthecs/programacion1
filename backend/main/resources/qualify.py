from flask_restful import Resource
from flask import request, jsonify

from main.auth.decorators import admin_required, poet_required
from .. import db
from main.models import QualifyModel

#Poem resources
class Qualify(Resource):
    
    def get(self, id):
        
        qualify = db.session.query(QualifyModel).get_or_404(id)
        return qualify.to_json_short()

    @poet_required
    def put(self, id):
        qualify = db.session.query(QualifyModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(qualify, key, value)
        db.session.add(qualify)
        db.session.commit()
        return qualify.to_json() , 201

    
    @admin_required
    @poet_required
    def delete(self, id):
        
        qualify = db.session.query(QualifyModel).get_or_404(id)
        db.session.delete(qualify)
        db.session.commit()
        return '', 204

    
    

class Qualifications(Resource):
    
    def get(self):
        qualifications = db.session.query(QualifyModel).all()  
        return jsonify([qualify.to_json_short() for qualify in qualifications])
    
    @poet_required
    def post(self):
        qualify = QualifyModel.from_json(request.get_json())
        db.session.add(qualify)
        db.session.commit()
        return qualify.to_json_short(), 201

    
        
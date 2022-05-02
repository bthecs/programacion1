from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import QualifyModel

#Poem resources
class Qualify(Resource):
    
    def get(self, id):
        
        qualify = db.session.query(QualifyModel).get_or_404(id)
        return qualify.to_json()

    
    def put(self, id):
        qualify = db.session.query(QualifyModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(qualify, key, value)
        db.session.add(qualify)
        db.session.commit()
        return qualify.to_json() , 201

    
    
    def delete(self, id):
        
        qualify = db.session.query(QualifyModel).get_or_404(id)
        db.session.delete(qualify)
        db.session.commit()
        return '', 204

    
    

class Qualifications(Resource):
    
    def get(self):
        page = 1
        per_page = 10
        qualifications = db.session.query(QualifyModel)
        
        
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                #paginate
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
                if key == "score":
                    score = score.filter(QualifyModel.score == value)
                if key == "comment":
                    comment = comment.filter(QualifyModel.comment.like("%" + value + "%"))
                if key == "user":
                    user_id = user_id.filter(QualifyModel.user_id == value)
                if key == "poem":
                    poem_id = poem_id.filter(QualifyModel.poem_id == value)
                
                #Order
                if key == "sort_by":
                    if value == "score":
                        score = score.order_by(QualifyModel.score)
                    if value == "score[desc]":
                        score = score.order_by(QualifyModel.score.desc())
                    if value == "user":
                        user = user.order_by(QualifyModel.user_id)
                    if value == "user[des]":
                        user = user.order_by(QualifyModel.user_id.desc())
                    if value == "poem":
                        poem = poem.order_by(QualifyModel.poem_id)
                    if value == "poem[des]":
                        poem = poem.order_by(QualifyModel.poem_id.desc())
                        
                
        qualifications = qualifications.paginate(page, per_page, False, 30)
        return jsonify({
            "poems" : [qualifications.to_json_short() for qualify in qualifications.items],
            "total" : qualifications.total,
            "pages" : qualifications.pages,
            "page" : page
            
            })
    
    def post(self):
        qualify = QualifyModel.from_json(request.get_json())
        db.session.add(qualify)
        db.session.commit()
        return qualify.to_json(), 201

    
        
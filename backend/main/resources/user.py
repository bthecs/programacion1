from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import admin_required
from .. import db
from main.models import UserModel
from main.mail.functions import sendMail




#Poem resources
class User(Resource):
    
    #Obtener el recurso
    #@jwt_required()
    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user.to_json_complete()
        
        #Verifica el Usuario
        # identity = get_jwt_identity()
        
        # if identity:
        #     return user.to_json_short()
        # else:
        #     return user.to_json_pulic()
            

    @admin_required
    @jwt_required()
    def put(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user.to_json() , 201


    
    @jwt_required()
    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204


class Users(Resource):
    
    #@admin_required
    def get(self):
        page = 1
        per_page = 10
        
        users = db.session.query(UserModel)
        
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == "name":
                    name = name.filter(UserModel.name.like("%"+ value +"%"))
                if key == "email":
                    email = email.filter(UserModel.email.like("%"+ value +"%"))

                #Order
                if key == "sort_by":
                    if value == "name":
                        name = name.order_by(UserModel.name)
                    if value == "name[des]":
                        name = name.order_by(UserModel.name.desc())
                    if value == "email":
                        email = email.order_by(UserModel.email)
                    if value == "email[desc]":
                        email = email.order_by(UserModel.email.desc())
                    if value == "date":
                        date = date.order_by(UserModel.date)
                    if value == "date[desc]":
                        date = date.order_by(UserModel.date.desc())
                    if value == "num_poems":
                        num_poems = num_poems.order_by(UserModel.num_poems)
                    if value == "num_qualifications":
                        num_qualifications = num_qualifications.order_by(UserModel.num_qualifications)
        
        users = users.paginate(page=page, per_page=per_page, error_out=False)
        return jsonify({
            "users" : [user.to_json_short() for user in users.items],
            "total" : users.total,
            "pages" : users.pages,
            "page" : page
            
            })
    

    #@admin_required
    def post(self):
        
        user = UserModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        sendMail(user.email, 'Bienvenido a Poet', 'mail/new_poem', user=user)
        return user.to_json(), 201

    
        
from .. import db



class Qualify(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    score = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id") ,nullable = False)
    poem_id = db.Column(db.Integer, db.ForeignKey("poem.id") ,nullable = False)
    
    user = db.relationship('User', back_populates="qualifications",uselist=False,single_parent=True)
    poems = db.relationship('Poem', back_populates="qualifications",uselist=False,single_parent=True)
    
    
    def __repr__(self):
        return '<Qualify: %r %r %r %r >' % (self.score, self.comment, self.user_id, self.poem_id)    

    
    
    def to_json(self):
        poems = poems.to_json_short()
        user = [user.to_json_complete() for user in self.user]
        qualify_json = {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'role': self.role,
            'email': self.email,
            'score': self.score,
            'user': user,
            'poem': poems
        }
        return qualify_json
        
    
    def to_json_short(self):
        qualify_json = {
            'id': self.id,
            'score': self.score,
            'comment': self.comment,
            'user_id': self.user_id,
            'poem_id': self.poem_id
        }
        return qualify_json
    
    @staticmethod
    def from_json(qualify_json):
        id = qualify_json.get('id')
        score = qualify_json.get('score')
        comment = qualify_json.get('comment')
        user_id = qualify_json.get('user_id')
        poem_id = qualify_json.get('poem_id')
        return Qualify(id=id,
                    score=score,
                    comment=comment,
                    user_id=user_id,
                    poem_id=poem_id
                    )
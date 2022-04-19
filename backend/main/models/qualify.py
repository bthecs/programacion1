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
        qualify_json = {
            'id': self.id,
            'score': int(self.score),
            'comment': str(self.comment),
            'user_id': self.user.to_json(),
            'poem_id': self.poems.to_json()
        }
        return qualify_json
    
    def to_json_complete(self):
        poems = [poem.to_json() for poem in self.poems]
        user = [users.to_json() for users in self.user]
        qualify_json = {
            'id': self.id,
            'name': str(self.name),
            'password': str(self.password),
            'rol': str(self.rol),
            'email': str(self.email),
            'poems':poems,
            'user':user
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
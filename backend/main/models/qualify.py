from .. import db


class Qualify(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    score = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer, nullable = False)
    poem_id = db.Column(db.Integer, nullable = False)
    
    
    def __repr__(self):
        return '<Qualify: %r %r %r %r >' % (self.score, self.comment, self.user_id, self.poem_id)    

    
    def to_json(self):
        qualify_json = {
            'id': self.id,
            'score': int(self.score),
            'comment': str(self.comment),
            'user_id': int(self.user_id),
            'poem_id': int(self.poem_id)
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
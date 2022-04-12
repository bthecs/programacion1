from .. import db
from sqlalchemy.sql import func


class Poem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer)
    body = db.Column(db.String(100), nullable = False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    
    def __repr__(self):
        return '<Poem: %r %r %r %r >' % (self.title, self.user_id, self.body, self.date)    

    
    def to_json(self):
        poem_json = {
            'id': self.id,
            'title': str(self.title),
            'user_id': int(self.user_id),
            'body': str(self.body),
        }
        return poem_json
    
    @staticmethod
    def from_json(poem_json):
        id = poem_json.get('id')
        title = poem_json.get('title')
        user_id = poem_json.get('user_id')
        body = poem_json.get('body')
        return Poem(id=id,
                    title=title,
                    user_id=user_id,
                    body=body,
                    )
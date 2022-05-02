from datetime import datetime
from email.policy import default
from sqlalchemy import column
from .. import db
import datetime


class Poem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    body = db.Column(db.String(100), nullable = False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user = db.relationship('User', back_populates="poems",uselist=False,single_parent=True)
    qualifications = db.relationship("Qualify", back_populates="poems", cascade="all, delete-orphan")
    
    
    def __repr__(self):
        return '<Poem: %r %r %r %r >' % (self.title, self.user_id, self.body, self.date)    

    
    def to_json(self):
        poem_json = {
            'id': self.id,
            'title': str(self.title),
            'user': self.user.to_json(),
            'body': str(self.body),
            'date': str(self.date.strftime("%d-%m-%Y")),
            'qualifications': int(self.qualifications)
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
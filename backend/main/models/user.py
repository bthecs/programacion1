from .. import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    rol = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    
    
    def __repr__(self):
        return '<User: %r %r %r %r >' % (self.name, self.password, self.rol, self.email)    

    
    def to_json(self):
        user_json = {
            'id': self.id,
            'name': str(self.name),
            'password': str(self.password),
            'rol': str(self.rol),
            'email': str(self.email)
        }
        return user_json
    
    
    def to_json_short(self):
        user_json = {
            'id': self.id,
            'email': str(self.email)
        }
    
    @staticmethod
    def from_json(user_json):
        id = user_json.get('id')
        name = user_json.get('name')
        password = user_json.get('password')
        rol = user_json.get('rol')
        email = user_json.get('email')
        return User(id=id,
                    name=name,
                    password=password,
                    rol=rol,
                    email=email
                    )
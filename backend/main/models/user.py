from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    rol = db.Column(db.String(100), nullable = False, default="user")
    email = db.Column(db.String(100),unique = True, index=True, nullable = False)
    
    poems = db.relationship("Poem", back_populates="user",cascade="all, delete-orphan")
    qualifications = db.relationship("Qualify", back_populates="user", cascade="all, delete-orphan")
    
    
    #Getter de la contraseña plana no permite leerla
    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    #Setter de la contraseña toma un valor en texto plano
    #calcula el hash y lo guarda en el atributo password
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
        
    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,password):
        print(f"Password: {password}, Self.password: {self.password}")
        return check_password_hash(self.password, password)

    
    
    def __repr__(self):
        return '<User: %r %r %r %r >' % (self.name, self.password, self.rol, self.email)    

    def to_json_public(self):
        user_json = {
            'id': self.id,
            'name': str(self.name)
        }
        return user_json
    
    def to_json(self):
        user_json = {
            'id': self.id,
            'name': str(self.name),
            'password': str(self.password),
            'rol': str(self.rol),
            'email': str(self.email)
        }
        return user_json
    
    def to_json_complete(self):
        poems = [poem.to_json() for poem in self.poems]
        qualifications = [qualify.to_json() for qualify in self.qualifications]
        user_json = {
            'id': self.id,
            'name': str(self.name),
            'password': str(self.password),
            'rol': str(self.rol),
            'email': str(self.email),
            'poems':poems,
            'qualifications':qualifications,
            'num_poems':len(poems),
            'num_qualifications':len(qualifications)
        }
        return user_json
    def to_json_short(self):
        user_json = {
            'id': self.id,
            'name': str(self.name),
            'email': str(self.email)
        }
        return user_json
    
    
    @staticmethod
    def from_json(user_json):
        id = user_json.get('id')
        name = user_json.get('name')
        password = user_json.get('password')
        rol = user_json.get('rol')
        email = user_json.get('email')
        return User(id=id,
                    name=name,
                    plain_password=password,
                    rol=rol,
                    email=email
                    )
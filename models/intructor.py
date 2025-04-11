from mongoengine import * 
from models.sena import NombreSena
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from models.sena import NombreSena

bcrypt = Bcrypt()  

class NombreIntructor(Document):
    nombrecompleto =StringField(max_length=80,required=True)
    correoelectronico =StringField(max_length=80,required=True)
    centro = ReferenceField(NombreSena, required=True)
    password = StringField(required=True)
    
    
    def _repr__(self):
        return self.nombrecompleto
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):

        return bcrypt.check_password_hash(self.password, password)
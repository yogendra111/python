from app import ma
from models import User


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'password')


userSchema = UserSchema()
usersSchema = UserSchema(many=True)

from AuthAPIs import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'password')


userSchema = UserSchema()
usersSchema = UserSchema(many=True)

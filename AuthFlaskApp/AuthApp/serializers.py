from . import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'username', 'password', 'role')


userSchema = UserSchema()
usersSchema = UserSchema(many=True)


class BlogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date')


blogSchema = BlogSchema()
blogsSchema = BlogSchema(many=True)

from AuthApp import app, db
from AuthApp.decorators import token_required
from AuthApp.modals import Blog
from AuthApp.serializers import blogSchema, blogsSchema

from flask import request, jsonify


@app.route('/blog', methods=['POST'])
@token_required
def add_blog(current_user):
    data = request.get_json()
    new_blog = Blog(title=data['title'], description=data['description'])
    db.session.add(new_blog)
    db.session.commit()
    return blogSchema.jsonify(new_blog)


@app.route('/blog', methods=['GET'])
@token_required
def get_all_blogs(current_user):
    blogs = Blog.query.all()
    return blogsSchema.jsonify(blogs)


@app.route('/blog/<blog_id>', methods=['GET'])
@token_required
def get_blog(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    if not blog:
        return jsonify({"error": f"no blog found with id = {blog_id}"}), 404

    return blogSchema.jsonify(blog)


@app.route('/blog/<int:blog_id>', methods=['DELETE'])
@token_required
def delete_blog(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    if not blog:
        return jsonify({"error": f"no blog found with id = {blog_id}"}), 404

    db.session.delete(blog)
    db.session.commit()
    return jsonify({"Deleted blog": {"id": blog.id, "title": blog.title}})

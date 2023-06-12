from flask import render_template
from app.posts import bp
from app.models.post import Post


@bp.route('/')
def index():
    return render_template('posts/index.html')


@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')

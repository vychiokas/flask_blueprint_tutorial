from flask import render_template
from app.questions import bp
from app.models.question import Question


@bp.route('/')
def index():
    return render_template('questions/index.html')

from flask import Blueprint, render_template
from . import db
from flask_login import current_user, login_required


bp = Blueprint('main', __name__)


@bp.get('/')
def index():
    return render_template('index.html')


@bp.get('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

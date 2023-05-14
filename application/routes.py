from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from bot.bot import send_message
from flask_login import current_user, login_required


bp = Blueprint('main', __name__)


@bp.get('/')
def index():
    return render_template('index.html')


@bp.get('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@bp.route('/contact', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        message = request.form.get('message')
        send_message(username, email, message)
        return render_template('success_sended.html')
    else:
        return render_template('contact_form.html')
from flask import Blueprint, render_template

user = Blueprint('user', __name__)

@user.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)

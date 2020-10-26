from flask import Blueprint
from flask import request
from flask import session
from flask import render_template
from .forms import LoginForm, RegisterForm

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    return render_template('user.html', form=loginForm, heading='Login')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    registrationForm = RegisterForm()
    return render_template('user.html', form=registrationForm, heading='Register')
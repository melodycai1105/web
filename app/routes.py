from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.forms import RegistrationForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask import request
from app import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)




@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    form = LoginForm()
    return render_template('volunteer.html', form=form)



@app.route('/user', methods=['GET', 'POST'])
def user():
    form = LoginForm()
    return render_template('user.html', form=form)

@app.route('/perosnalpage', methods=['GET', 'POST'])
def personalpage():
    return render_template('personalpage.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('volunteer'))
    return render_template('register.html', title='Register', form=form)

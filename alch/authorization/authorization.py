from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from alch.exe import db
from alch.usefull.DataBase import Register, Users
from alch.usefull.forms import LoginForm, RegisterForm
from alch.exe import login_manager
from flask_login import login_user, UserMixin
from alch.usefull.userLogin import UserLogin

# from alch.usefull.userLogin import UserLogin

authorization = Blueprint('authorization', __name__, template_folder='templates', static_folder='static')

@login_manager.user_loader
def load_user(user_id):
    print('load_user')
    return Register.query.filter_by(login=RegisterForm.login.data).first()

# Готовая форма
@authorization.route('/register', methods=('POST', 'GET'))
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                hash = generate_password_hash(form.psw.data)
                r = Register(login=form.login.data, email=form.email.data, psw=hash)
                db.session.add(r)
                db.session.commit()
                return render_template('login.html')
            except:
                db.session.rollback()
    return render_template('register.html', title='Регистрация', form=form)


# Готовая форма
@authorization.route('/login', methods=('POST', 'GET'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = []
            user = Register.query.filter_by(login=form.login.data).first()
            if user and check_password_hash(user.psw, form.psw.data):
                print(user)
                login_user(user)
                return redirect(url_for('admin.profile'))
            else:
                flash('Неверный логин или пароль', 'error')
                return render_template('login.html', form=form)
    else:
        print('Ошибка подключения к БД')
        return render_template('login.html', form=form)

# @authorization.route('/register')
# def register():
#     return render_template('register.html')

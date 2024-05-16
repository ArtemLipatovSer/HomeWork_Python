from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from visit_card.db import db
from visit_card.usefull.DataBase import Register, Users
from visit_card.usefull.forms import LoginForm, RegisterForm
from visit_card.db import login_manager
from flask_login import login_user


# from visit_card.usefull.userLogin import UserLogin

authorization = Blueprint('authorization', __name__, template_folder='templates', static_folder='static')

@login_manager.user_loader
def load_user(user_id):
    return Register.query.get(int(user_id))

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
                db.session.flush()
                p = Users(lastname='', firstname='', specialty='', aboutMe='', numberPhone='',
                          vk='', email='', telegram='', insta='', user_id=r.id)
                db.session.add(p)
                db.session.commit()
                return redirect('login')
            except:
                db.session.rollback()
    return render_template('register.html', title='Регистрация', form=form)


@authorization.route('/login', methods=('POST', 'GET'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = []
            user = Register.query.filter_by(login=form.login.data).first()
            if user and check_password_hash(user.psw, form.psw.data):
                login_user(user)
                return redirect(url_for('admin.profile'))
            else:
                flash('Неверный логин или пароль', 'error')
                return render_template('login.html', form=form)
    else:
        print('Ошибка подключения к БД')
        return render_template('login.html', form=form)



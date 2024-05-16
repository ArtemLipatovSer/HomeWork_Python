from flask import Flask, render_template, abort
import os
from visit_card.admin.admin import admin
from visit_card.authorization.auth import authorization
import os.path
from visit_card.db import db, login_manager
from visit_card.usefull.DataBase import Register, Users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qweqweqweqwe'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'visits.db')
db.init_app(app)

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(authorization, url_prefix='/authorization')
login_manager.init_app(app)
login_manager.login_view = 'authorization.login'
login_manager.login_message = 'Необходима авторизация'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<username>')
def visitCard(username):
    p = Register.query.filter_by(login=username).first()
    img = os.path.exists(f'admin\static\img\{username}.jpg')
    if p:
        info = Users.query.filter_by(user_id=p.id).first()
        phone = '+' + ''.join(filter(str.isdigit, info.numberPhone))
        return render_template('visit_card.html', info=info, username=username, phone=phone, img=img)
    return abort(404)

@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title="Страница не найдена")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # with app.app_context():
    #     db.create_all()

# Осталось сделать удаление и 404 ошибку

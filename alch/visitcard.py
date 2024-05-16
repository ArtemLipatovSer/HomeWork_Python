from flask import Flask, render_template
from alch.admin.admin import admin
from alch.authorization.authorization import authorization
import os.path
from alch.exe import db, login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qweqweqweqwe'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'visits.db')
db.init_app(app)

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(authorization, url_prefix='/authorization')
login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # with app.app_context():
    #     db.create_all()

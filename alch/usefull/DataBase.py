from alch.exe import db


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<profiles {self.login}>'

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    specialty = db.Column(db.String(50), nullable=False)
    aboutMe = db.Column(db.String(1000))
    numberPhone = db.Column(db.String(50), nullable=False)
    vk = db.Column(db.String(50))
    email = db.Column(db.String(50))
    telegram = db.Column(db.String(50))
    insta = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey('register.id'))

    def __repr__(self):
        return f'<profiles {self.id}>'



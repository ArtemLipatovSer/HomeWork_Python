from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from visit_card.usefull.DataBase import Register


class UniqueUsernameValidator:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        login = Register.query.filter_by(login=field.data).first()
        email = Register.query.filter_by(email=field.data).first()
        if login or email:
            raise validators.ValidationError(self.message)


class LoginForm(FlaskForm):
    login = StringField('Username')
    psw = PasswordField('Password')
    # remember = BooleanField('Запомнить: ', default=False)
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    login = StringField('Имя: ',
                        validators=[DataRequired(), Length(max=30, message='Логин должен содержать до 30 символов'),
                                    UniqueUsernameValidator(message='Такой логин уже существует')])
    email = StringField('Email: ', validators=[Email('Некорректный email'), UniqueUsernameValidator(message='Эта почта уже зарегистрирована')])
    psw = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=4, max=100,
                                                                       message='Пароль должен содержать от 4 до 100 символов')])
    psw2 = PasswordField('Пароль: ', validators=[DataRequired(), EqualTo('psw', message='Пароли должны совпадать')])
    submit = SubmitField('Зарегистрировать')


class ProfileForm(FlaskForm):
    lastName = StringField('Фамилия', validators=[DataRequired()])
    firstName = StringField('Имя', validators=[DataRequired()])
    spec = StringField('Специальность', validators=[DataRequired()])
    aboutMe = TextAreaField('О себе', validators=[Length(max=500, message='Максимум 500 символов')])
    numberPhone = StringField('Номер телефона')
    vkontakte = StringField('Вконтакте')
    email = StringField('Эл. почта: ', validators=[Email('Некорректный email')])
    telegram = StringField('Телеграмм')
    submit = SubmitField('Отправить')

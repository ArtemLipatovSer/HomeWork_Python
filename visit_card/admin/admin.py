from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, current_user
from visit_card.usefull.forms import ProfileForm
from visit_card.usefull.DataBase import Users, Register
from flask_login import logout_user
from visit_card.db import db
import os

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


@admin.route('/profile', methods=('POST', 'GET'))
@login_required
def profile():
    p = Users.query.filter_by(user_id=current_user.id).first()
    form = ProfileForm()
    name = current_user.login
    if request.method == 'POST':
        file = request.files['file']
        file.filename = f'{name}.jpg'
        if file:
            file.save(os.path.join('admin\static\img', file.filename))
        p = Users.query.filter_by(user_id=current_user.id).first()
        if form.validate_on_submit():
            p.lastname = form.lastName.data
            p.firstname = form.firstName.data
            p.specialty = form.spec.data
            p.aboutMe = form.aboutMe.data
            p.numberPhone = form.numberPhone.data
            p.vk = form.vkontakte.data
            p.email = form.email.data
            p.telegram = form.telegram.data
            db.session.commit()
            return redirect(url_for('visitCard', username=name))
        return render_template('profile.html', form=form)
    if p:
        form.lastName.data = p.lastname
        form.firstName.data = p.firstname
        form.spec.data = p.specialty
        form.aboutMe.data = p.aboutMe
        form.numberPhone.data = p.numberPhone
        form.vkontakte.data = p.vk
        form.email.data = p.email
        form.telegram.data = p.telegram
        img = os.path.exists(f'admin\static\img\{name}.jpg')
        return render_template('profile.html', form=form, img=img, name=name)
    return render_template('profile.html', form=form)


@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@admin.route('/delete')
def delete():
    name = current_user.login
    p = Register.query.filter_by(id=current_user.id).first()
    db.session.delete(p)
    db.session.commit()
    logout_user()
    os.remove(f'admin\static\img\{name}.jpg')
    return redirect(url_for('index'))

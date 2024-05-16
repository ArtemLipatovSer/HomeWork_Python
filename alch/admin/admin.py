from flask import Blueprint, request, render_template
from alch.usefull.forms import ProfileForm
from alch.usefull.DataBase import Register, Users


admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

@admin.route('/profile', methods=('POST', 'GET'))
def profile():
    form = ProfileForm()
    u = Register.query.get(1)
    print(u)
    if request.method == 'POST':
        # if form.validate_on_submit():
            # try:
            #     hash = generate_password_hash(form.psw.data)
            #     r = Register(login=form.login.data, email=form.email.data, psw=hash)
            #     db.session.add(r)
            #     db.session.commit()
            #     return render_template('profile.html')
            # except:
            #     db.session.rollback()
        return render_template('profile.html', form=form)
    return render_template('profile.html', form=form)

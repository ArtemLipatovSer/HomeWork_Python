from flask import Flask, render_template, request, flash

app = Flask(__name__)
SECRET_KEY = 'qweqweqweqwe'
app.config['SECRET_KEY'] = 'qweqweqweqwe'

style = [
    'css/bootstrap.min.css',
    'css/unicons.css',
    'css/owl.carousel.min.css',
    'css/owl.theme.default.min.css',
    'css/tooplate-style.css'
]

script = [
    'js/jquery-3.3.1.min.js',
    'js/popper.min.js',
    'js/bootstrap.min.js',
    'js/Headroom.js',
    'js/jQuery.headroom.js',
    'js/owl.carousel.min.js',
    'js/smoothscroll.js',
    'js/custom.js'
]

menu = [
    {"name": "About", "url": "#about"},
    {"name": "Project", "url": "#project"},
    {"name": "Resume", "url": "#resume"},
    {"name": "Contact", "url": "#contact"}
]

info_men = ['Artem Lipatov', 'WebDeveloper', 'Fullstack']

project_info = [
    {'url': 'images/project/project-image01.png'},
    {'url': 'images/project/project-image02.png'},
    {'url': 'images/project/project-image03.png'},
    {'url': 'images/project/project-image04.png'},
    {'url': 'images/project/project-image05.png'}
]

experience = [
    {'year': 2019, 'speciality': 'Project Manager', 'place_of_work': 'Best Studio', 'comment': 'Proin ornare non purus '
    'ut rutrum. Nulla facilisi. Aliquam laoreet libero ac pharetra feugiat. Cras ac fermentum nunc, a faucibus nunc.'},
    {'year': 2018, 'speciality': 'UX Designer', 'place_of_work': 'Best Studio', 'comment': 'Fusce rutrum augue id '
    'orci rhoncus molestie. Nunc auctor dignissim lacus vel iaculis.'},
    {'year': 2016, 'speciality': 'UI Freelancer', 'place_of_work': 'Best Studio', 'comment': 'Sed fringilla vitae enim '
    'sit amet cursus. Sed cursus dictum tortor quis pharetra. Pellentesque habitant morbi tristique senectus et '
    'netus et malesuada fames ac turpis egestas.'},
    {'year': 2014, 'speciality': 'Junior Designer', 'place_of_work': 'Crafted Co.', 'comment': 'Cras scelerisque '
    'scelerisque condimentum. Nullam at volutpat mi. Nunc auctor ipsum eget magna consequat viverra.'}
]

education = [
    {'year': 2017, 'speciality': 'Mobile Web', 'school': 'Master Design', 'comment': 'Please tell your friends '
    'about Tooplate website. That would be very helpful. We need your support.'},
    {'year': 2015, 'speciality': 'User Interfaces', 'school': 'Creative Agency', 'comment': 'is a great website to '
    'download HTML templates without any login or email.'},
    {'year': 2021, 'speciality': 'Artwork Design', 'school': 'New Art School', 'comment': 'You can freely use '
     'Tooplate\'\s templates for your business or personal sites. You cannot redistribute this template without a permission.'}
]


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if len(request.form['name']) >= 3 and \
                len(request.form['name']) >= 5 and \
                '@' in request.form['email'] and \
                len(request.form['message']) >= 5:
            flash('Сообщение доставлено', category='success')
        else:
            flash('Ошибка', category='error')
    return render_template("index.html", style=style, script=script, menu=menu, info_men=info_men, project_info=project_info, experience=experience, education=education)


if __name__ == "__main__":
    app.run(debug=True)

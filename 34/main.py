import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort
from useful.dbClass import dbClass

app = Flask(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'posts.db')))
app.config['SECRET_KEY'] = 'qweqweqweqwe'


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/allPosts')
def allPosts():
    db = get_db()
    dbase = dbClass(db)
    return render_template('allPosts.html', posts=dbase.getPostAnonce(), title='Посты')


@app.route('/add_post', methods=['GET', 'POST'])
def addPost():
    db = get_db()
    dbase = dbClass(db)
    print('hello')
    if request.method == 'POST':
        if len(request.form['title']) > 4 and len(request.form['textPost']) > 10:
            res = dbase.addPost(request.form['title'], request.form['author'], request.form['url'],
                                request.form['textPost'])
            if not res:
                flash('Ошибка добавления', category='error')
            else:
                flash('Добавлено', category='success')
        else:
            flash('Ошибка добавления, проверьте ваши данные', category='error')
    return render_template('add_post.html', title='Добавление поста')


@app.route('/post/<alias>')
def showPost(alias):
    db = get_db()
    dbase = dbClass(db)
    post = dbase.getPost(alias)
    if not post:
        abort(404)
    return render_template('post.html', title=post['title'], post=post)


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена')


if __name__ == '__main__':
    create_db()
    app.run(debug=True)

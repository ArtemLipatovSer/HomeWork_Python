import sqlite3
from flask import url_for


class dbClass:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addPost(self, title, author, url, textPost):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM posts WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Пост с данным URL уже есть!')
                return False
            self.__cur.execute('INSERT INTO posts VALUES(NULL,?,?,?,?)', (title, author, url, textPost))
            self.__db.commit()
        except:
            print('Error adding post')
            return False
        return True

    def getPost(self, alias):
        try:
            self.__cur.execute(f'SELECT id, title, textPost, author from posts WHERE url like ? LIMIT 1', (alias,))
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print(f'Ошибка при получении поста из БД + {e}')
        return []

    def getPostAnonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, author, url, textPost from posts')
            res = self.__cur.fetchall()
            print(res)
            if res:
                return res
        except sqlite3.Error as e:
            print(f'Ошибка при получении постов из БД + {e}')
        return []

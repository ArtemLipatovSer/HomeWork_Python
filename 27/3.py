def stringUser():
    def tag(str):
        return f'<h1>{str}</h1>'
    return tag

cnt = stringUser()
print(cnt("Python"))

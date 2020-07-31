from flask_script import Manager
from flask import Flask, request, make_response, redirect, abort


app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return redirect('http://www.baidu.com')


# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__=='__main__':
    manager.run()

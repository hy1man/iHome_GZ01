#coding:utf-8

from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manage =Manager(app)
a=1

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    manage.run()
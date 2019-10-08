from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SECRET_KEY'] = '8b97b12a5d0c1bfae26c67abcd59448c46d64fe7456846ca80c6d6f700a379ec'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db =SQLAlchemy(app)
bcrypt =Bcrypt(app)

from flasktodo import routes
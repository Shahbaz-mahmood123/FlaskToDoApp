from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from flasktodo.config import Config

app = Flask(__name__)
app.config['SECRET_KEY']=   '8b97b12a5d0c1bfae26c67abcd59448c46d64fe7456846ca80c6d6f700a379ec'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
#app.config.from_object(Config)
db =SQLAlchemy(app)
bcrypt =Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view= 'users.login'
login_manager.login_message_category = 'info'




from flasktodo.users.routes import users
from flasktodo.lists.routes import lists
from flasktodo.main.routes import main 

app.register_blueprint(users)
app.register_blueprint(lists)
app.register_blueprint(main)



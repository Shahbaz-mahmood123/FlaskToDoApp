from flasktodo  import db, login_manager
from datetime import datetime
from flask_login import UserMixin   

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable= False)
    email = db.Column(db.String(120), unique=True, nullable= False)
    image_file = db.Column(db.String(20),  nullable= False, default= 'default.jpg')
    password = db.Column(db.String(60), nullable= False, default= datetime.utcnow)
    lists = db.relationship('Lists', backref='ListAuthor', lazy = True)
    
    #need to change models so user_id is just id and the same for all other primary keys in table as to call userid in routes the column should be ID. 
    #Also helps in stopping repeating calling user.user_id etc
    def get_id(self):
           return (self.user_id)

    def __repr__(self):
        return f"User ('{self.username}', '{self.email}', '{self.image_file}')"

class Lists(db.Model):
    listid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable= False)
    date_created  = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    content = db.Column(db.Text , nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable =False)

    def get_id(self):
        return (self.user_id)

class Tasks(db.Model):
    task_id = db.Column(db.Integer, primary_key = True)
    date_created  = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    content = db.Column(db.Text , nullable= False)
    Action_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Text, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable =False)
    listid = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable =False)
    
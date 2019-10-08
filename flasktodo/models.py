from flasktodo  import db
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable= False)
    email = db.Column(db.String(120), unique=True, nullable= False)
    image_file = db.Column(db.String(20),  nullable= False, default= 'default.jpg')
    password = db.Column(db.String(60), nullable= False, default= datetime.utcnow)
    lists = db.relationship('Lists', backref='ListAuthor', lazy = True)

    def __repr__(self):
        return f"User ('{self.username}', '{self.email}', '{self.image_file}')"

class Lists(db.Model):
    listid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable= False)
    date_created  = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    content = db.Column(db.Text , nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable =False)

# class Tasks(db.Model):
#     task_id = db.Column(db.Integer, primary_key = True)
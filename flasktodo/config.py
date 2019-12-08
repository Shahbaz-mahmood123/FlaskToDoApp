import os


class Config:
        # TODO Setting enviornment variables not working, might need to restart laptop. Try below code again after restarting
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
# app.config['SECRET_KEY']=   '8b97b12a5d0c1bfae26c67abcd59448c46d64fe7456846ca80c6d6f700a379ec'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
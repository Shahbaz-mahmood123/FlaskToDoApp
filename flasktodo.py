from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8b97b12a5d0c1bfae26c67abcd59448c46d64fe7456846ca80c6d6f700a379ec'

posts = [
    {
        'user': 'Shahbaz Mahmood',
        'title': 'List1',
        'content': 'first todo list',
        'date_posted': 'today',
    },

    {
        'user': 'test test',
        'title': 'test',
        'content': 'test todo list',
        'date_osted': 'yesterday',  
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form =form)

@app.route('/register', methods =['GET', 'POST'])
def register():
    form= RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Blueprint
from flask import render_template, request, Blueprint
from flasktodo.models import Lists
from flask_login import current_user, login_required
from flasktodo.models import User, Lists

main= Blueprint('main', __name__)

#pagination is not working, getting error that the pagination orbject is not iterable?

@main.route('/home')
@login_required
def home():
    user_id = current_user.get_id()
    page = request.args.get('page', 1, type =int)
    #lists= Lists.query.paginate( page=page, per_page=2)
    lists= Lists.query.filter_by(user_id = user_id).paginate(page=page, per_page=6  )
    return render_template('home.html', lists = lists)

@main.route('/')
@main.route('/about')
def about():
    return render_template('about.html')

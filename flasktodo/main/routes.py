from flask import Blueprint
from flask import render_template, request, Blueprint
from flasktodo.models import Lists

main= Blueprint('main', __name__)

#pagination is not working, getting error that the pagination orbject is not iterable?
@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type =int)
    lists= Lists.query.paginate( page=page, per_page=2)
    #lists= Lists.query.all()
    return render_template('home.html', lists = lists)


@main.route('/about')
def about():
    return render_template('about.html')

from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flasktodo import db
from flasktodo.models import Lists
from flasktodo.lists.forms import ListForm

lists= Blueprint('lists', __name__)

@lists.route("/list/new", methods=['GET', 'POST'])
@login_required
def new_list():
    form = ListForm()
    if form.validate_on_submit():
        list=Lists(title =form.title.data, content = form.content.data, user_id = current_user.get_id())
        db.session.add(list)
        db.session.commit()
        flash('New list has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_list.html', title ='New List', form = form,  legend= 'New List')


@lists.route("/list/<int:list_id>", methods=['GET', 'POST'])
@login_required
def list(list_id):
    lists =Lists.query.get_or_404(list_id)
    return render_template('list.html', title=lists.title, lists=lists)

@lists.route("/list/<int:list_id>/update", methods=['GET', 'POST'])
@login_required
def update_list(list_id):
    lists =Lists.query.get(list_id)
    form = ListForm()
    if lists.user_id != current_user.get_id():
        abort(403)
    if form.validate_on_submit():
        lists.title = form.title.data
        lists.content = form.content.data
        db.session.commit()
        flash('Your list has been updated')
        return redirect(url_for('lists.list', list_id = list_id))
        ##issue with this route  not working properly, redirectig to list page without showing the update form
    elif request.method == 'GET':
        form.title.data = lists.title
        form.content.data=lists.content  
    return render_template('create_list.html', title ='Update List', form = form, legend= 'Update List' )


@lists.route("/list/<int:list_id>/delete", methods=['POST'])
@login_required
def delete_list(list_id):
    list = Lists.query.get_or_404(list_id)
    db.session.delete(list)
    db.session.commit()
    flash('List has been deleted')
    return redirect(url_for('main.home'))


@lists.route("/lists1", methods=['GET', 'POST'])
def lists1():
    return render_template('lists1.html')

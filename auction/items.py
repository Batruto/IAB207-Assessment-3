from flask import Blueprint
from flask import request
from flask import session
from flask import redirect, url_for
from flask import render_template

from .models import ItemInfo, Comment, User
from .forms import CommentForm
from . import db

from .forms import ItemForm

bp = Blueprint('item', __name__, url_prefix='/items')

@bp.route('/<id>')
def view_item(id):
    item = item = ItemInfo.query.filter_by(id=id).first()
    cform = CommentForm()
    return render_template("items/show.html", item = item, form = cform)

    ss

# def check_upload_file(form):
#     # get file data from form
#     fp = form.image.data
#     filename = fp.filename
#     # get the current path of the module file... store image file relative to this path
#     BASE_PATH = os.path.dirname(__file__)
#     # upload file location - directory of this file/static/image
#     upload_path = os.path.join(BASE_PATH, 'static/Images', secure_filename(filename))
#     # store relative path in DB as image location in HTML is relative
#     db_upload_path = '/static/Images/' + secure_filename(filename)
#     # save the file and return the db upload path
#     fp.save(upload_path)
#     return db_upload_path

@bp.route('/create', methods = ['GET', 'POST'])
#@login_required #decorator between the route and view function
def create():
  form = ItemForm()
  if form.validate_on_submit():
    # if the form was successfully submitted
    # access the values in the form data
    item = ItemInfo(name=form.name.data, 
                description=form.description.data,
                image=form.image.data,
                currency=form.currency.data)
    # add the object to the db session
    db.session.add(item)
    # commit to the database
    db.session.commit()

    #flash('Successfully created new travel destination', 'success')
    print('Successfully created new travel destination', 'success')
    return redirect(url_for('item.create'))

  return render_template('items/create.html', form=form)


@bp.route('/<item>/comment', methods = ['GET', 'POST"'])
#@login_required
def comment(item):
    form = CommentForm()
    # get the item object associated to the page
    item_obj = ItemInfo.query.filter_by(id=item).first()
    if form.validate_on_submit():
        # read the comment form the form
        comment = Comment(text=form.text.data, item = item_obj)#,
                           # user = current_user)

        # here the back-referencing works - comment.item is set
        # and teh link is created
        db.session.add(comment)
        db.session.commit()

        # flashing a message which needs to be handled by the html
        # flash ('Your comment has been added', 'success')
        print('Your comment has been added', 'success')
    # using redirect sends a GET request to item.show
    return redirect(url_for('item.show', id=item))

# USE CODE LATER
def get_item():
    return None
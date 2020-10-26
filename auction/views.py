from flask import Blueprint
from flask import request
from flask import session
from flask import render_template

from .models import ItemInfo

from .forms import CommentForm, ItemForm

#from .models import Destination

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    return render_template('index.html')

# @mainbp.route('/item-create')
# def item_create():
#     return render_template('Item_Creation.html')

# @mainbp.route('/item-details')
# def item_details():
#     return render_template('View_Items.html')

# @mainbp.route('/Watchlist')
# def watchlist():
#     return render_template('WatchListGame.html')


# route to allow users to search
@mainbp.route('/search')
def search():
    #get the search string from request
    if request.args['search']:
        dest = "%" + request.args['search'] + '%'
        #use filter and like function to search for matching destinations
        items = ItemInfo.query.filter(ItemInfo.name.like(dest)).all()
        #render index.html with few destinations
        return render_template('index.html', items=items)
    else:
        return redirect(url_for('main.index'))

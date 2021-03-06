from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')


# class ItemInfo(db.Model):
#     __tablename__ = 'iteminfo'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(100), index = True, unique = True, nullable = False)
#     description = db.Column(db.String(200))
#     current_bid = db.Column(db.String(6))
#     minimum_bid = db.Column(db.String(6))
#     image = db.Column(db.String(400))
    
#     comments = db.relationship('Comment', backref = 'item')
#     #reviews = db.Integer



#     def __repr__(self): #string print method
#             return "<Name: {}>".format(self.name)


class ItemInfo(db.Model):
    __tablename__ = 'iteminfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='item')

    
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    iteminfo_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    

    def __repr__(self):
            return "<Comment: {}>".format(self.text)

class ItemBids(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(8))
    bidded_at = db.Column(db.DateTime, default = datetime.now())
    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('iteminfo.id'))

from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

# variable which holds the types of files allowed to use
ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field


    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

class ItemForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  # adding two validators, one to ensure input is entered and other to check if the 
  #description meets the length requirements
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  #create a filefield that takes two validators - File required and File Allowed
  image = FileField('Destination Image', validators=[FileRequired(message='Image can not be empty'),
                                         FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
   
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")

# class ItemForm(FlaskForm):
#     # create a filefield that takes two validators - File Required and File Allowed
#     #image = FileField('Item Upload', validators=[FileRequired(message = 'Image can not be empty'),
#     #                                        FileAllowed(ALLOWED_FILE, message = 'Only support png, jpg, JPG, PNG, bmp')])

#     name = StringField('Item', validators=[InputRequired()])
#     # adding two validators, one to ensure the input is entered and other
#     # to check if the description meets the length requirements
#     description = TextAreaField('Description', validators = [InputRequired()])

#     platform = SelectField('Platform', validate_choice = True)

#     condition = SelectField('Condition', validate_choice = True)
    

#     #minimum_bid = StringField('Minimum Bid', validators = [InputRequired()])
#     submit = SubmitField('Create')

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')
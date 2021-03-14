'''
All forms for the website
'''

from flask_uploads import IMAGES, UploadSet
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, PasswordField, StringField, TextAreaField, SelectField
from wtforms.validators import (DataRequired, Email, Length, ValidationError,
                                equal_to, regexp)

import Ecommerce.models as models

images = UploadSet('images', IMAGES)


def email_exists(form, field):
    if models.User.select().where(models.User.email == field.data).exists():
        raise ValidationError('User with email already exists')

class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email(),email_exists])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6), equal_to('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    mobile_no = IntegerField('Mobile No', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class BannerForm(FlaskForm):
    image = FileField('Load Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    mobile_no = IntegerField("Mobile No", validators=[DataRequired()])
    message = TextAreaField('Your Message', validators=[DataRequired()])

class new_product_form(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    image_1 = FileField('Smallest Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    image_2 = FileField('Medium Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    image_3 = FileField('Large Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    count = IntegerField('Product Count', validators=[DataRequired()])
    actual_price = IntegerField('Product Price')
    off_percent = IntegerField('Off Percent %')
    buy_price = IntegerField('Buy Price')
    features = StringField('Features')
    overview_eng = StringField('Overview English')
    overview_de = StringField('Overview Germany')
    other_details = TextAreaField('Other Details')
    category = SelectField('Category', choices=[])



class edit_product_form(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    image_1 = FileField('Smallest Image', validators=[ FileAllowed(images, 'Images only!')])
    image_2 = FileField('Medium Image', validators=[FileAllowed(images, 'Images only!')])
    image_3 = FileField('Large Image', validators=[FileAllowed(images, 'Images only!')])
    count = IntegerField('Product Count', validators=[DataRequired()])
    actual_price = IntegerField('Product Price')
    off_percent = IntegerField('Off Percent %')
    buy_price = IntegerField('Buy Price')
    features = StringField('Features')
    overview_eng = StringField('Overview English')
    overview_de = StringField('Overview Germany')
    other_details = TextAreaField('Other Details')
    category = SelectField('Category', choices=[])


class Checkout_form(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    room_no = StringField('Room no', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mobile = IntegerField("Mobile No", validators=[DataRequired()])

class new_password(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6), equal_to('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

class new_review(FlaskForm):
    user = StringField('User')
    order_id = StringField('Order-ID')
    text = TextAreaField('Review')

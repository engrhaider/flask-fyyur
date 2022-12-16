from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL
from wtforms.validators import Regexp
from enums import *
from validations import *

class ShowForm(Form):
     state = SelectField(
            'state', validators=[DataRequired(message='state required')],
             choices=[(state.value, state.name) for state in State]
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired(message='Start time required')],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired(DataRequired(message='name required'))]
    )
    city = StringField(
        'city', validators=[DataRequired(DataRequired(message='city required'))]
    )
    state = SelectField(
        'state', validators=[DataRequired(message='state required')],
         choices=[(state.value, state.name) for state in State]
    )
    address = StringField(
        'address', validators=[DataRequired(message='address required')]
    )
    phone = StringField(
        'phone', validators=[Regexp(r'^\d{3}-\d{3}-\d{4}$', message="Phone number must be in the format '123-456-7890'")]
    )
    image_link = StringField(
        'image_link', validators=[URL(message='Invalid image link')]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired(message='genres required'), validate_genres],
        choices=[(genre.value, genre.name) for genre in Genre],
   )
    facebook_link = StringField(
        'facebook_link', validators=[URL(message='Invalid facebook link')]
    )
    website_link = StringField(
        'website_link', validators=[URL(message='Invalid website link')]
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )



class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired(message='name required')]
    )
    city = StringField(
        'city', validators=[DataRequired(message='city required')]
    )
    state = SelectField(
          'state', validators=[DataRequired(message='state required')],
          choices=[(state.value, state.name) for state in State]
    )
    phone = StringField(
        'phone', validators=[Regexp(r'^\d{3}-\d{3}-\d{4}$', message="Phone number must be in the format '123-456-7890'")],
    )
    image_link = StringField(
        'image_link', validators=[URL(message='Invalid image link')]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired(message='genres required'), validate_genres],
         choices=[(genre.value, genre.name) for genre in Genre]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(message='Invalid facebook link')]
     )

    website_link = StringField(
        'website_link', validators=[URL(message='Invalid website link')]
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )


from enums import *
from enums import *
from wtforms import ValidationError

def validate_genres(form, field):
    if not all(genre in [g.value for g in Genre] for genre in field.data):
        raise ValidationError("Only the list of defined genres can be added")
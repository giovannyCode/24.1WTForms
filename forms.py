from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SelectField,TextAreaField ,BooleanField
from wtforms.validators import InputRequired, Optional, URL,Length, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine"),("hamster", "Hamster")])
    photo_url = StringField("URL",validators=[Optional(),URL()])
    age = IntegerField("Age",validators=[Optional(),NumberRange(min=0, max=30)])
    notes = TextAreaField( "Notes",  validators=[Optional(), Length(min=10)])
   

class PetForm(FlaskForm):
    """Form for editing a pet."""
    photo_url = StringField( "Photo URL", validators=[Optional(), URL()] )
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")


   
 

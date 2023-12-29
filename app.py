from flask import Flask, request, render_template, redirect,flash, session ,json,jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, PetForm
app = Flask(__name__)
app.config['SECRET_KEY'] ="oh-so-secret"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)
"""db.drop_all()
db.create_all()"""
 
@app.route("/")
def home():
    pets =Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""
    form = AddPetForm()
    print("I am in the method")
    if form.validate_on_submit():
        print("I am inside of if")
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes =form.notes.data
        pet = Pet(name =name,species = species,photo_url =photo_url, age =age , notes= notes ) 
        db.session.add(pet)
        db.session.commit()
        flash(f"{name} of {species} species has  been updated", 'success')
        return redirect("/")
    else:
        print("did not get in the if")
        return render_template("pet_add_form.html", form=form)
    
@app.route("/pet/<int:pet_id>/edit",methods=["GET","POST"])
def pet_edit  (pet_id):
    """Show pet edit form and handle edit."""
    pet =Pet.query.get_or_404(pet_id) 
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet.name} of {pet.species} species has  been updated", 'success')
        return redirect("/")
    else:
        return render_template("pet_edit.html", form=form,pet=pet)

    








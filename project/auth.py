from cgi import print_exception
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from  . import User, db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.adminhome'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.adminhome'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
         flash('     address already exists')

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/reservation')
def reservation():
    return render_template('reservation.html') 

@auth.route('/reservation', methods=['POST'])
def reservation_post():
    name =request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    time = request.form.get('time')
    # obj = Reservation(name=name, email=email, phone=phone, time=time)

@auth.route('/admin/menu')
def menu_admin():
    return render_template('menufaiz.html')

@auth.route('/form/menu')
def menu_form():
    return render_template('form.html')

# @auth.route('/form/menu', methods=['POST'])
# def menu_tambah():
#     name = request.form.get('name')
#     description = request.form.get('description')
#     price = request.form.get('price')


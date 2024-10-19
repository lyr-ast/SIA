from flask import Flask, render_template, jsonify, request, flash, Blueprint, url_for, redirect
from . import db
from .models import User
from flask_bcrypt import Bcrypt
from flask_login import login_user, login_required, logout_user, current_user


app = Flask(__name__)
bcrypt = Bcrypt(app)

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')


        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):

                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='danger')
        else:
            flash('Email does not exist.', category='danger')

    return render_template("sign_in.html", user=current_user)



@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirm-password')
        
        user = User.query.filter_by(email=email).first()       

        if confirmPassword != password:
            flash("Passwords don't match", "danger")
            return redirect(url_for("auth.signup"))
        
        elif user:
            flash('Email address already exists', category='danger') 
            return redirect(url_for("auth.signup"))
        
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='danger')
        
        elif len(username) < 5:
            flash('First name must be greater than 4 characters.', category='danger')

        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='danger')
        

        else:

            new_user = User(email=email, username=username, password=bcrypt.generate_password_hash(password))   

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))



@auth.route('/otp', methods=["GET", "POST"])
def otp():
    return render_template('otp.html')  # OTP page
 


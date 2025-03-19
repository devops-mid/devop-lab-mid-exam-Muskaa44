from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User
from datetime import datetime
import re

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')  # Optional field
    dob_str = request.form.get('dob', '')  # Get DOB from form

    # Validate email format
    email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if not re.match(email_pattern, email):
        flash("Invalid email format!", "danger")
        return redirect(url_for('index'))

    # Validate phone number (must be 10 digits)
    if phone and not re.match(r'^\d{10}$', phone):
        flash("Phone number must be exactly 10 digits!", "danger")
        return redirect(url_for('index'))

    # Validate Date of Birth (DOB should not be in the future)
    if dob_str:
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            if dob > datetime.today().date():
                flash("Date of Birth cannot be in the future!", "danger")
                return redirect(url_for('index'))
        except ValueError:
            flash("Invalid Date of Birth format!", "danger")
            return redirect(url_for('index'))
    else:
        dob = None  # Handle cases where DOB is not provided

    # Create new user with DOB
    user = User(name=name, email=email, phone=phone, dob=dob)
    db.session.add(user)
    db.session.commit()
    
    flash("User successfully registered!", "success")
    return redirect(url_for('index'))


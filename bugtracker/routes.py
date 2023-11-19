from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from bugtracker import db, bcrypt, login_manager
from bugtracker.forms import RegistrationForm, LoginForm, PostIssueForm
from bugtracker.models import User, Post

bugtracker_bp = Blueprint('bugtracker', __name__)


@bugtracker_bp.route("/")
@bugtracker_bp.route("/home")
def home():
    users = User.query.all()
    posts = Post.query.all()
    return render_template('home.html', users=users, current_user=current_user, posts=posts)


@bugtracker_bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(
            FirstName=form.FirstName.data,
            LastName=form.LastName.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Account created for {}!".format(form.username.data), 'success')
        return redirect(url_for('bugtracker.login'))
    return render_template('register.html', title='Register', form=form)


@bugtracker_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('bugtracker.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('bugtracker.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@bugtracker_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('bugtracker.home'))


@bugtracker_bp.route("/issue", methods=['GET', 'POST'])
@login_required
def postissue():
    form = PostIssueForm(request.form)
    if request.method == "POST":
        assigned_user = User.query.filter(
            User.username.ilike(form.AssignedTo.data),
            User.AccessToken != current_user.AccessToken
        ).first()

        print(assigned_user)
        print("Assigned To:", form.AssignedTo.data)
        print("Current User Access Token:", current_user.AccessToken)

        if assigned_user:
            post = Post(
                title=form.Title.data,
                Description=form.Description.data,
                AssignedTo=form.AssignedTo.data,
                Createdby=current_user.username,
                Status=form.Status.data
            )
            assigned_user.notification += 1
            db.session.add(post)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('bugtracker.home'))
        else:
            flash('Invalid Assignment. Please try again.', 'danger')
    return render_template('issue.html', title='New Issue', current_user=current_user, form=form)

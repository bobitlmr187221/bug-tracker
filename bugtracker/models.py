from datetime import datetime
from bugtracker import db
'''
Email,Username,FirstName,LastName, Password, AccessToken
'''


class User(db.Model):
    __tablename__ = 'user'
    AccessToken = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    notification = db.Column(db.Integer, default=0)
    posts = db.relationship('Post',  lazy=True)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "User('{}', '{}','{}','{}','{}')".format(self.username, self.email, self.AccessToken, self.password, self.notification)

    def get_id(self):
        return str(self.AccessToken)

    def is_authenticated(self):
        return self.id is not None

    def is_active(self):
        return self.is_authenticated()

    def is_anonymous(self):
        return not self.is_authenticated()


'''Title, Description, AssignedTo (User relation), 
Createdby (User relation), Status (Open, Closed) '''


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    Description = db.Column(db.String(100), nullable=False)
    AssignedTo = db.Column(db.String(20), nullable=False)
    Createdby = db.Column(db.Integer, db.ForeignKey(
        'user.AccessToken'), nullable=False)
    Status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "Post('{}','{}', '{}','{}','{}','{}')".format(self.id, self.title, self.date_posted, self.Createdby, self.AssignedTo, self.date_posted)

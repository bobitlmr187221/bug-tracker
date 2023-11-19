class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # Disable Flask-SQLAlchemy modification tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#!/usr/bin/env python3

from flask_login import LoginManager
from bugtracker import create_app, db
from flask_migrate import Migrate
from bugtracker.models import User

app = create_app()
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True)

<<<<<<< HEAD
# Bug Tracker
> A simple issue tracking web application built using Python, Flask, SQLAlchemy,Flask_bcrypt,Flaskwtf and FlaskWtforms.


## Description

> This application provides a user with a functionality to create, read, update and delete a bug/issue.


# How to run

```
1. open terminal and direct it to the locations where the Bug-Tracker is located. 

2. Run the below command.
      a. pip3 install -r requirements.txt 
      b. email_validator
      c. go to http://127.0.0.1:5000/ 
      
3. To create new database for the user
    a. follow the first step
    b. type 'python' in terminal
      b1. from bugtracker import db
      b2. from bugtracker.models import User, Post
      b3. User.query.delete()
      b4. Post.query.delete()
      b5. from bugtracker import db
      b6. from bugtracker.models import User, Post
      b7. db.session.commit()
      b8. exit()

4. To close the debug feature
   a. open run.py
   b. make 'debug=True' to 'debug=False' in app.run
  
```

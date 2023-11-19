# Bug Tracker
> A simple issue tracking web application built using Python, Flask, SQLAlchemy,Flask_bcrypt,Flaskwtf and FlaskWtforms.


## Description

> This application provides a user with a functionality to create, read, update and delete a bug/issue.


# How to run

```
1. open terminal and direct it to the locations where the Bug-Tracker is located. 

2. Run the below command.
      a. pip3 install -r requirements.txt 
      b. flask db init
      c. flask db migrate -m "Your Migration Message"
      d. flask db upgrade
   -- Then run the application as follows:
      ./app.py

4. To close the debug feature
   a. open run.py
   b. make 'debug=True' to 'debug=False' in app.run
  
```

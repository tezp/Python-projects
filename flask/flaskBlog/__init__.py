import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreteKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db?check_same_thread=False'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = str('enterYourEmail@gmail.com')  # os.environ.get('GMAIL_USERNAME')
app.config['MAIL_PASSWORD'] = str('Password')  # os.environ.get('GMAIL_PASSWORD')
app.config['MAIL_DEBUG'] = True
mail = Mail(app)

from flaskBlog.users.route import users
from flaskBlog.posts.route import posts
from flaskBlog.main.route import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)


from flask import Flask,render_template,session,redirect,url_for,flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
import os
from flask.ext.script import Shell
from flask.ext.mail import Mail
from flask.ext.mail import Message
import smtplib  
from email.mime.text import MIMEText 
from threading import Thread
from config import config
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown

login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'
bootstrap=Bootstrap()
mail=Mail()
moment=Moment()
db=SQLAlchemy()
pagedown=PageDown()

def create_app(config_name):
	app=Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	pagedown.init_app(app)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint,url_prefix='/auth')
	from .api_1_0 import api as api_1_0_blueprint
	app.register_blueprint(api_1_0_blueprint,url_prefix='/api/v1.0') 
	
	return app
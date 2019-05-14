from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import Login
@app.route('/')
@app.route('/index')
def index():
	return render_template("base.html",title='Home')
@app.route('/login',methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit() and request.method == 'POST':
		flash('Login successful!')
		return render_template("base.html",title="Home")
	return  render_template("form.html",title='Login',form=form)
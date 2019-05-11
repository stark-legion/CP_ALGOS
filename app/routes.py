from flask import render_template, flash, redirect
from app import app
from app.forms import Login
@app.route('/')
@app.route('/index')
def index():
	return render_template("base.html",title='Home')
@app.route('/login',methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		flash('Login successful for username {}, remember= {}'.format(form.username.data,form.remember.data))
		return redirect('/index')
	return  render_template("form.html",title='Login',form=form)
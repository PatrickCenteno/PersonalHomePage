from HomePage import app
from flask import render_template

@app.route('/')
def index():
	#TODO display the index.html template
	return render_template('index.html', response='HERES MY PAGE!')

@app.route('/resume')
def show_resume():
 	#TODO show the resume page 
	return 'Here\'s my resume'

@app.route('/projects')
def show_projects():
	return 'list of projects'

@app.route('/admin')
def admin_page():
	return 'Admin page goes here'
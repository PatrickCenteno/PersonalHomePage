from HomePage import app
from flask import render_template

import database

@app.route('/')
def index():
	#TODO display the index.html template
	return render_template('index.html')

@app.route('/education')
def show_education():
 	#TODO show the resume page 
	return 'Here\'s my resume'

@app.route('/projects')
def show_projects():
	return 'list of projects'

@app.route('/work')
def show_work():
	return 'work'

@app.route('/language')
def show_languages():
	return 'languages'

@app.route('/admin')
def admin_page():
	#will have all info from db passed into it
	courses = database.get_courses()
	languages = database.get_languages()
	projects = database.get_projects()
	work = database.get_work_experience()

	return render_template('admin.html', course_list=courses, language_list=languages, \
			project_list=projects, work_list=work)
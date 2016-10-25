from HomePage import app
from flask import render_template

import database

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
	#will have all info from db passed into it
	courses = database.get_courses()
	languages = database.get_languages()
	projects = database.get_projects()
	work = database.get_work_experience()
	for c in courses:
		print c 
	for l in languages:
		print l 
	for p in projects:
		print p
	for w in work:
		print w 

	return render_template('admin.html', course_list=courses, language_list=languages, \
			project_list=projects, work_list=work)
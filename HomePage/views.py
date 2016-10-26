from HomePage import app
from flask import render_template

import database

@app.route('/')
def index():
	#TODO display the index.html template
	return render_template('index.html')

@app.route('/education')
def show_education():
	courses = database.get_courses()
	return render_template('education.html', course_list=courses)

@app.route('/projects')
def show_projects():
	projects = database.get_projects()
	return render_template('projects.html', project_list=projects)

@app.route('/work')
def show_work():
	work = database.get_work_experience()
	return render_template('work.html', work_list=work)

@app.route('/languages')
def show_languages():
	languages = database.get_languages()
	return render_template('languages.html', language_list=languages)

@app.route('/contact')
def show_contact_page():
	return render_template('contact.html')

@app.route('/admin')
def admin_page():
	#will have all info from db passed into it
	courses = database.get_courses()
	languages = database.get_languages()
	projects = database.get_projects()
	work = database.get_work_experience()

	return render_template('admin.html', course_list=courses, language_list=languages, \
			project_list=projects, work_list=work)
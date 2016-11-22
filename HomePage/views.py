from HomePage import app
from flask import render_template, make_response, request
from datetime import date, datetime
import time

import database

''' gets cookie of timestamp for last date date visited 
	sets that string as jira var to display on page 
	gets current timestamp and replaces cookie with that date'''
@app.route('/')
def index():
	old_timestamp = request.cookies.get('date_visited')
	response = make_response(render_template('index.html', date_visited=old_timestamp))
	timestamp = get_time_and_date()
	response.set_cookie('date_visited', timestamp)
	return response

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

# funtion to get time an date to store as cookie
def get_time_and_date():
	# bool var to determine if am or pm is displayed
	show_am = True

	t = time.localtime(time.time())
	month = t.tm_mon
	day = t.tm_mday
	year = t.tm_year
	hour = t.tm_hour
	min = t.tm_min

	# uses % to conver 24 hour time to 12 hour time
	if hour > 12:
		hour = t.tm_hour % 12
		show_am = False

	# Properly formats time to ensure theres a '0'
	# infront of single digit minutes
	if min < 10:
		min = "0" + str(t.tm_min)
		
	if show_am:
		return str(hour) + ":" + str(min) + " AM, " + str(month) + "/" + str(day) + "/" + str(year)
	else:
		return str(hour) + ":" + str(min) + " PM, " + str(month) + "/" + str(day) + "/" + str(year)

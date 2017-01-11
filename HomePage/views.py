from HomePage import app
from flask import render_template, make_response, request, session
from datetime import date, datetime
import time, os, hashlib

import database

# Must retreive primary and sceondary color for every route

''' gets cookie of timestamp for last date date visited 
	sets that string as jira var to display on page 
	gets current timestamp and replaces cookie with that date'''
@app.route('/')
def index():
	colors = database.get_colors()
	for c in colors:
		print str(c[1]) + " " + str(c[2])

	old_timestamp = request.cookies.get('date_visited')
	response = make_response(render_template('index.html', date_visited=old_timestamp, color_list=colors))
	timestamp = get_time_and_date()
	response.set_cookie('date_visited', timestamp)
	return response

@app.route('/education')
def show_education():
	colors = database.get_colors()
	courses = database.get_courses()
	return render_template('education.html', course_list=courses, color_list=colors)

@app.route('/projects')
def show_projects():
	colors = database.get_colors()
	projects = database.get_projects()
	return render_template('projects.html', project_list=projects, color_list=colors)

@app.route('/work')
def show_work():
	colors = database.get_colors()
	work = database.get_work_experience()
	return render_template('work.html', work_list=work, color_list=colors)

@app.route('/languages')
def show_languages():
	colors = database.get_colors()
	languages = database.get_languages()
	return render_template('languages.html', language_list=languages, color_list=colors)

@app.route('/contact')
def show_contact_page():
	colors = database.get_colors()
	return render_template('contact.html', color_list=colors)

@app.route('/admin')
def admin_page():
	# Displays the password modal
	# Function is api.py contains logic about what to do upon entry of password
	return render_template('modalDisplay.html')

@app.route('/admin_display')
def admin_display():
	# requires session to be set for it to work
	if session['successful_load'] == 'true':
		# obtain all necessary information for the admin page and 
		# render the admin template
		#will have all info from db passed into it
		courses = database.get_courses()
		languages = database.get_languages()
		projects = database.get_projects()
		work = database.get_work_experience()
		colors = database.get_colors()

		# Remove session
		session['successful_load'] = 'false'
		return render_template('admin.html', course_list=courses, language_list=languages, \
				project_list=projects, work_list=work)
	else:
		return 'You are not authorized to access this page'
	


# #temporary view
# @app.route('/addColorToDB')
# def add_color_sql():
# 	#database.add_colors_table()
# 	colors = database.get_colors()

# 	print 'Testing if colors is loaded'
# 	for c in colors:
# 		print c
# 	return 'printing to console'

# @app.route('/setColors/<colorOne>/<colorTwo>')
# def set_colors(colorOne, colorTwo):
# 	database.set_color(colorOne, colorTwo)
# 	return 'test color numbers set'




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

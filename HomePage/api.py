from HomePage import app
from flask import render_template, request, redirect, session
import database

import uuid
import hashlib
 
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

# Accepts the password as a POST var
@app.route('/check_password', methods=['POST'])
def check_password():
	#get password from db
	pass_from_db = database.get_password()

	#gets hashed and salt
	hashed_pass, salt = pass_from_db[0][0].split(':')

	#get Post var of raw password
	if request.method == 'POST':
		password = request.form['password']
	else:
		return 'No password supplied'

	#hash and check with salt
	if hashed_pass == hashlib.sha256(salt.encode() + password.encode()).hexdigest():
		session['successful_load'] = 'true'
		return 'correct password'
	else:
		return 'incorrect password'

# Adds information based on table name what content is provided
@app.route('/add_info', methods=['POST'])
def add_info():
	#table name 
	table = request.form['table_name']
	if table == 'courses':
		database.add_course(request.form['course_name'])
		return 'course added'
	elif table == 'languages':
		database.add_language(request.form['language'])
		return 'language added'
	elif table == 'projects':
		database.add_project(request.form['project_description'], request.form['link'])
		return 'project added'
	elif table == 'work_experience':
		database.add_work_experience(request.form['place'], request.form['location'], \
				request.form['time_period'], request.form['role'], request.form['description'])
		return 'Work Info added'
	elif table == 'colors':
		database.set_color(request.form['color_one'], request.form['color_two'])
		return 'colors changed'
	else:
		return 'invalid post request'

#delete information based on id number and table name
@app.route('/delete_info', methods=['POST'])
def delete_info():
	#table name
	table = request.form['table_name']
	id_num = request.form['id_num']
	if table == 'courses':
		database.delete_course(id_num)
		return 'course removed'
	elif table == 'languages':
		database.delete_language(id_num)
		return 'language removed'
	elif table == 'projects':
		database.delete_project(id_num)
		return 'project added'
	elif table == 'work_experience':
		database.delete_work(id_num)
		return 'Work Info removed'
	else:
		return 'invalid post request'
	


# @app.route('/add_table')
# def add_table():
# 	db = database.get_db()
# 	db.execute('ALTER TABLE projects ADD link text')
# 	db.commit()
# 	return 'added link to projects'

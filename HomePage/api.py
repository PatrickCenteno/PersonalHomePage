from HomePage import app
from flask import render_template, request
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
		return 'password correct'
	else:
		return 'incorrect password'

# Adds information based on table name what content is provided
@app.route('/add_info', methods=['POST'])
def add_info():
	#table name 
	table = request.form['table_name']
	if table == 'courses':
		database.add_cours(request.form['course_name'])
		return 'course added'
	elif table == 'languages':
		database.add_language(request.form['language'])
		return 'language added'
	elif table == 'projects':
		database.add_project(request.form['project_description'])
		return 'project added'
	else:
		return 'invalid post request'

	#TODO add work experience - its a little more complex 
from HomePage import app
from flask import Flask, request, g, session, redirect, url_for, abort, \
     render_template, flash
import sqlite3

''' BoilerPlate code to setup, initializes and return a connection to db throughout app '''
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

''' All Database functions go here '''

''' Adding functions '''

#temporary add table function
# def add_colors_table():
# 	db = get_db()
# 	db.execute('create table colors( id integer primary key autoincrement, colorOne integer not null, colorTwo integer nut null )')
# 	db.commit()
# 	print 'color table query was executed'

# #temporary function
# def add_pass_to_db(password):
# 	db = get_db()
# 	db.execute('INSERT into pass(password) values (?)', (password, ))
# 	db.commit()

#Add work experience field
def add_work_experience(place, location, time_period, role, description):
	db = get_db()
	db.execute('INSERT into work_experience (place, location, time_period, role, description) values (?,?,?,?,?)', \
		(place, location, time_period, role, description))
	db.commit()
	return 'Added job'

#Add course
def add_course(course):
	db = get_db()
	db.execute('INSERT into courses (course_name) values(?)', (course,))
	db.commit()
	return 'Added course'

#Add language
def add_language(language):
	db = get_db()
	db.execute('INSERT into languages (language) values(?)', (language, ))
	db.commit()
	return 'Added language'

#Add project
def add_project(project, link):
	db = get_db()
	db.execute('INSERT into projects (project_description , link) values(?, ?)', (project, link, ))
	db.commit()
	return 'Added project' 

#Set the two colors for the site
def set_color(color_one, color_two):
	db = get_db()

	# Remove whatever colors are stored in there currently
	db.execute('DELETE FROM colors')
	db.commit()

	# Store current colors
	db.execute('INSERT into colors (colorOne, colorTwo) values(?, ?)', (color_one, color_two, ))
	db.commit()


''' Get Functions '''

#Gets all courses
def get_courses():
	db = get_db()
	cursor = db.execute('SELECT * FROM courses')
	return cursor.fetchall()

#Gets all languages
def get_languages():
	db = get_db()
	cursor = db.execute('SELECT * FROM languages')
	return cursor.fetchall()

#Gets all work experience
def get_work_experience():
	db = get_db()
	cursor = db.execute('SELECT * FROM work_experience')
	return cursor.fetchall()

#Gets all projects
def get_projects():
	db = get_db()
	cursor = db.execute('SELECT * FROM projects')
	return cursor.fetchall()

def get_password():
	db = get_db()
	cursor = db.execute('SELECT password FROM pass')
	return cursor.fetchall()

def get_colors():
	db = get_db()
	cursor = db.execute('SELECT * FROM colors')
	return cursor.fetchall()

''' Delete Functions '''

#Table truncating function
#There is no truncate command in sqlite. This can hopefully be implemented on the live server
#when Postgresql or MySql is being utilized
#If there are no entries in the table, it truncates it so the auto-increment id resets
def truncate_table(table_name, db):
	size = db.execute('SELECT MAX(ID) FROM ?', (table_name, ))
	if size == 0:
		db.execute('TRUNCATE ?', (table_name, ))


#delete course by id
def delete_course(id_num):
	db = get_db()
	print str(id_num) + 'inside db function'
	db.execute('DELETE FROM courses WHERE ID = ?', (id_num, ))
	db.commit()
	# truncate_table('courses', db)
	return 'Deleted course with id of ' + str(id_num)

#delete language by id
def delete_language(id_num):
	db = get_db()
	db.execute('DELETE FROM languages WHERE ID = ?', (id_num, ))
	db.commit()
	# truncate_table('languages', db)
	return 'Deleted language with an id of' + str(id_num)

#delete work by id
def delete_work(id_num):
	db = get_db()
	db.execute('DELETE FROM work_experience WHERE ID = ?', (id_num, ))
	db.commit()
	# truncate_table('work_experience', db)
	return 'Deleted work with id of ' + str(id_num)

#delete project by id
def delete_project(id_num):
	db = get_db()
	db.execute('DELETE FROM projects WHERE ID = ?', (id_num, ))
	db.commit()
	# truncate_table('projects', db)
	return 'Deleted project with an id of' + str(id_num)

from HomePage import app

@app.route('/')
def index():
	#TODO display the index.html template
	return 'Hello World!'

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
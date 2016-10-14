from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash
import os

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'main.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('HOMEPAGE_SETTINGS', silent=True)

import HomePage.views
import HomePage.database


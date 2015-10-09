import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost/cugc')
db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'Hello world'
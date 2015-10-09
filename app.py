import arrow
import datetime
import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost/cugc')
db = SQLAlchemy(app)

import models

@app.route('/')
def index():
    # Get next Friday
    today = datetime.date.today()
    friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
    friday = arrow.get(friday).format('MMMM D, YYYY')
    return render_template('index.html', meeting_date=friday)

if __name__ == '__main__':
    app.run(debug=True)

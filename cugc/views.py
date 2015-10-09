import arrow
import datetime
from flask import render_template, flash, redirect, session, url_for, request, \
    g, jsonify
from cugc import app
from .models import Game

@app.route('/')
def index():
    # Get next Friday
    today = datetime.date.today()
    friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
    friday = arrow.get(friday).format('MMMM D, YYYY')
    return render_template('index.html', meeting_date=friday)    

@app.route('/games')
@app.route('/games/<int:page>')
def games(page=1):
    return render_template('games.html', games=Game.query.paginate(page, 10, False))

@app.route('/admin')
def admin():
    return render_template('admin.html')

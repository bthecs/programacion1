from flask import Blueprint, render_template, url_for
from main.routes import user, poem
# Create a Blueprint object
app = Blueprint('main', __name__, url_prefix='/')

# Create a route for the home page
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_poem')
def add_poem():
    return render_template('add poem.html')

@app.route('/login')
def login():
    return render_template('login.html')

from flask import Blueprint, render_template,request




# Create a Blueprint object
author = Blueprint('user', __name__, url_prefix='/user')

users = [
    {"id":0 , 'name': 'User 1', 'email': 'lautarogimenez@gmail.com'},
]

@author.route('/')
def index():
    return render_template('profile.html')

# Create a route for the home page
@author.route('/user/<int:id>')
def profile(id=0):
    return render_template('profile.html', user=users[id])
    
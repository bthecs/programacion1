from flask import Blueprint, render_template,request
import requests
import json




# Create a Blueprint object
author = Blueprint('user', __name__, url_prefix='/user')


@author.route('/')
def index():
    return render_template('profile.html')

# Create a route for the home page
@author.route('/user/<int:id>', methods=['GET', 'POST'])
def profile():
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'GET':
            user_id = request.args.get('id')
            url = 'http://127.0.0.1:8500/user/' + user_id

            headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {cookie}'}

            response = requests.get(url, headers=headers)

            user = json.loads(response.text)

            return render_template('profile.html', user=user)
    return render_template('profile.html')
    
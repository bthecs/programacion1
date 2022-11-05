from email import header
from lib2to3.pgen2 import token
from urllib import response
from flask import Blueprint, make_response, render_template, url_for, request, redirect
import requests
import json
from main.routes import user, poem
# Create a Blueprint object
app = Blueprint('main', __name__, url_prefix='/')

# Create a route for the home page
@app.route('/')
def index():
    api_url = "http://127.0.0.1:8500/poemas"

    data = {"page": 1, "per_page": 10}

    headers = {"Content-Type": "application/json"}

    response = requests.get(api_url, data=json.dumps(data), headers=headers)
    print(response.status_code)
    print(response.text)

    poemas = json.loads(response.text)
    print(poemas)

    return render_template('home.html', poemas=poemas['poemas'])

    

@app.route('/add_poem')
def add_poem():
    return render_template('add poem.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email, password)

        api_url = "http://127.0.0.1:8500/auth/login"

        data = {"email": email, "password": password}

        headers = {"Content-Type": "application/json"}

        response = requests.post(api_url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            print(response.text)
            print(response.status_code)

            token = json.loads(response.text)
            token = token['access_token']
            print(token)

            resp = make_response(redirect(url_for('main.index')))
            resp.set_cookie('token', token)
            return resp
        else:
            return render_template('login.html', error='Email or password incorrect')
    return render_template('login.html')

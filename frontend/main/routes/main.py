from distutils.log import error
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
    url = 'http://127.0.0.1:8500/poeminfo'

    data = {"page": 1, "per_page": 10}

    headers = {'Content-type': 'application/json'}

    response = requests.get(url, json=data, headers=headers)

    poems = json.loads(response.text)


    return render_template('home.html', poems=poems["poem"])

    

@app.route('/add_poem', methods=['GET', 'POST'])
def add_poem():
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'POST':
            url = 'http://127.0.0.1:8500/poems'

            data = {"title": request.form['title'], "body": request.form['body'], "user_id": request.cookies.get('id')}

            headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {cookie}'}

            response = requests.post(url, json=data, headers=headers)

            print(response.text)

    
            # redirigir al poema creado
            return redirect(url_for('main.index'))
        else:
            return render_template('create_poem.html')
    else:
        return redirect(url_for('main.index'))       
            # response = requests.post(url, json=data, headers=headers)
            # print(response.text)


        

    return render_template('create_poem.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        api_url = 'http://localhost:8500/auth/login'

        data = {"email": email, "password": password}

        headers = {"Content-Type" : "application/json"}

        response = requests.post(api_url, json = data, headers = headers)

        

        if response.status_code == 200:
            response = json.loads(response.text)
            token = response["access_token"]
            user_id = str(response["id"])
            

            resp = make_response(redirect(url_for('main.index')))
            resp.set_cookie('access_token', token)
            resp.set_cookie("id", user_id)

            return resp
        else:
            return render_template('login.html')
    else:
        return render_template('login.html', error="Invalid email or password")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    resp = make_response(redirect(url_for('main.index')))
    resp.delete_cookie('access_token')
    resp.delete_cookie('id')
    return resp

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        email = request.form['email']
<<<<<<< HEAD
        api_url = 'http://localhost:8500/users'
=======
        api_url = 'http://localhost:8500/auth/register'
>>>>>>> ba62707 (crud update)

        data = {"name": user, "password": password,"rol": "user" ,"email": email}

        headers = {"Content-Type" : "application/json"}

        response = requests.post(api_url, json = data, headers = headers)

<<<<<<< HEAD
        if response.status_code == 201:
=======
        if response.status_code == 200:
>>>>>>> ba62707 (crud update)
            return redirect(url_for('main.login'))
        else:
            return render_template('register.html', error="Email already exists")
    return render_template('register.html')
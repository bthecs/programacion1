from flask import Blueprint, render_template,request, redirect, url_for, make_response
import requests
import json




# Create a Blueprint object
author = Blueprint('user', __name__, url_prefix='/user')


@author.route('/')
def index():
    cookie = request.cookies.get('access_token')
    if cookie:
        user_id = request.cookies.get('id')

        url = 'http://127.0.0.1:8500/user' + f'/{user_id}'

        headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {cookie}'}

        response = requests.get(url, headers=headers)

        user = json.loads(response.text)

        print(user)

        return render_template('profile.html', user=user)
    return render_template('profile.html')


@author.route('/<int:id>', methods=['GET'])
def user_view(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'GET':

            url = 'http://127.0.0.1:8500/user' + f'/{id}'

            headers = {'Content-type': 'application/json', 'Authorization': f"Bearer {cookie}"}

            response = requests.get(url, headers=headers)

            user = json.loads(response.text)

            print(user)

            return render_template('profile.html', user=user)
    else:
        return redirect(url_for('main.index'))
# # Create a route for the home page
# @author.route('/user/<int:id>', methods=['GET', 'POST'])
# def profile():
#     cookie = request.cookies.get('access_token')
#     if cookie:
#         if request.method == 'GET':
#             user_id = request.args.get('id')
#             url = 'http://127.0.0.1:8500/user/' + user_id

#             headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {cookie}'}

#             response = requests.get(url, headers=headers)

#             user = json.loads(response.text)

#             print(user)

#             return render_template('profile.html', user=user)
#     return render_template('profile.html')

#delete poem user

@author.route('/delete_poem/<int:id>', methods=['POST'])
def delete(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        url = 'http://127.0.0.1:8500/poem/' + f'{id}'
        headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {cookie}'}
        response = requests.delete(url, headers=headers)
        print(response.text)
        return redirect(url_for('main.index'))
    return redirect(url_for('main.index'))

#delete user

@author.route('/delete_user', methods=['POST'])
def delete_user():
    cookie = request.cookies.get('access_token')
    if cookie:
        user_id = request.cookies.get('id')
        url = 'http://127.0.0.1:8500/user/' + f'{user_id}'
        headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {cookie}'}
        response = requests.delete(url, headers=headers)
        print(response.text)
        return redirect(url_for('main.index'))
    return redirect(url_for('main.index'))


#update user
@author.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_poem(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'GET':

            url = 'http://127.0.0.1:8500/user/' + str(id)

            headers = {'Content-type': 'application/json', 'Authorization': f"Bearer {cookie}"}

            response = requests.get(url, headers=headers)

            user = json.loads(response.text)

            print(user)

            return render_template('profile_edit.html', user=user)
        elif request.method == 'POST':
            url = 'http://127.0.0.1:8500/user/' + str(id)

            data = {"name": request.form['name'], "email": request.form['email']}

            headers = {'Content-type': 'application/json', 'Authorization' : f"Bearer {cookie}"}

            response = requests.put(url, json=data, headers=headers)

            print(response.text)

            return redirect(url_for('main.index'))
    else:
        return redirect(url_for('main.index'))
    return render_template('profile_edit.html')        

        

    

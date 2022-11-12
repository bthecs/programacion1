from flask import Blueprint, render_template, redirect, url_for, request, make_response
import requests
import json


# Create a Blueprint object
poem = Blueprint('poem', __name__, url_prefix='/poem')

poems = [{"id":0 , 'title': 'Poem 1', 'body': 'This is the body of poem 1'}]

@poem.route('/')
def index():
    return render_template('poem_view.html')


# Create a route for the home page
@poem.route('/<int:id>', methods=['GET'])
def poem_view(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'GET':

            url = 'http://127.0.0.1:8500/poem/' + str(id)

            headers = {'Content-type': 'application/json', 'Authorization': f"Bearer {cookie}"}

            response = requests.get(url, headers=headers)

            poem = json.loads(response.text)

            print(poem)

            return render_template('poem_view.html', poem=poem)


@poem.route('/comment/<int:id>', methods=['POST'])
def comment(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'POST':
            user_id = request.cookies.get('id')            

            data = {"user_id": int(user_id), "poem_id": int(id), "score": int(request.form['star']), "comment": request.form['comment']}

            url = 'http://127.0.0.1:8500/qualifications'

            headers = {'Content-type': 'application/json', 'Authorization': f"Bearer {cookie}"}

            print(data)

            response = requests.post(url, json=data, headers=headers)


            return redirect(url_for('poem.poem_view', id=id))
        
    return redirect(url_for('user.login'))


@poem.route('/delete_comment/<int:id>', methods=['POST'])
def delete(id):
    print("hola")
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'POST':
            url = 'http://127.0.0.1:8500/qualify/' + str(id)

            headers = {'Content-type': 'application/json', 'Authorization': f"Bearer {cookie}"}

            response = requests.delete(url, headers=headers)

            print(response.text)

            return redirect(url_for('main.index'))

    return redirect(url_for('user.login'))

# Create a route delete comment
# @poem.route('/delete_comment/<int:id>', methods=['DELETE'])
# def delete_comment(id):
#     cookie = request.cookies.get('access_token')
#     if cookie:
#         if request.method == 'DELETE':
#             url = 'http://

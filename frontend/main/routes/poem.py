from flask import Blueprint, render_template, redirect, url_for, request, make_response
import requests
import json


# Create a Blueprint object
poem = Blueprint('poem', __name__, url_prefix='/poem')

# VISTA DE TODOS LOS POEMAS
@poem.route('/')
def index():
    return render_template('poem_view.html')


# VISTA DE UN POEMA
@poem.route('/<int:id>', methods=['GET'])
def poem_view(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'GET':

            url = 'http://127.0.0.1:8500/poem/' + str(id)

            headers = {'Content-type': 'application/json', 'Authorization': f"Bearer {cookie}"}

            response = requests.get(url, headers=headers)

            poem = json.loads(response.text)

            for i in poem['qualifications']:
                i['user_id'] = str(i['user_id'])
                

            poem['user']['id'] = str(poem['user']['id'])         


            return render_template('poem_view.html', poem=poem)
    else:
        return redirect(url_for('main.index'))



# VISTA DE CREAR COMENTARIO Y CALIFICACION
@poem.route('/comment/<int:id>', methods=['POST'])
def comment(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'POST':
            user_id = request.cookies.get('id')
           
           
            if request.form['comment'] != '' or  request.form['star'] != '':

                data = {"user_id": int(user_id), "poem_id": int(id), "score": int(request.form['star']), "comment": request.form['comment']}

                url = 'http://127.0.0.1:8500/qualifications'

                headers = {'Content-type': 'application/json', 'Authorization': f"Bearer {cookie}"}

                response = requests.post(url, json=data, headers=headers)
                print(response.text)
                return redirect(url_for('poem.poem_view', id=id))

            else:
                return redirect(url_for('poem.poem_view', id=id))       

        else:
            return redirect(url_for('poem.poem_view', id=id))
    else:
        return redirect(url_for('user.login'))



# ELIMINAR COMENTARIO
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

            return redirect(url_for('peom.poem_view', id=id))

        else:
            return redirect(url_for('poem.poem_view', id=id))
    else:
        return redirect(url_for('user.login'))



# EDITAR COMENTARIO
@poem.route('/edit_comment/<int:id>', methods=['POST'])
def edit(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'POST':
            url = 'http://127.0.0.1:8500/qualify/' + str(id)

            data = {"score": int(request.form['star'])}

            headers = {'Content-type': 'application/json', 'Authorization' : f"Bearer {cookie}"}

            response = requests.put(url, json=data, headers=headers)

            print(response.text)

            return redirect(url_for('main.index'))

    return redirect(url_for('user.login'))


# VISTA DE EDITAR POEMA
@poem.route('/edit_poem/<int:id>', methods=['GET', 'POST'])
def edit_poem(id):
    cookie = request.cookies.get('access_token')
    if cookie:
        if request.method == 'GET':

            url = 'http://127.0.0.1:8500/poem/' + str(id)

            headers = {'Content-type': 'application/json', 'Authorization': f"Bearer {cookie}"}

            response = requests.get(url, headers=headers)

            poem = json.loads(response.text)

            print(poem)

            return render_template('update_poem.html', poem=poem)

        if request.method == 'POST':
            url = 'http://127.0.0.1:8500/poem/' + str(id)

            data = {"title": request.form['title'], "body": request.form['body']}

            headers = {'Content-type': 'application/json', 'Authorization' : f"Bearer {cookie}"}

            response = requests.put(url, json=data, headers=headers)

            print(response.text)

            return redirect(url_for('main.index'))

    return redirect(url_for('user.login'))



            
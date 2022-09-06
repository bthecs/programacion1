from flask import Blueprint, render_template

# Create a Blueprint object
poem = Blueprint('poem', __name__, url_prefix='/poem')

poems = [{"id":0 , 'title': 'Poem 1', 'body': 'This is the body of poem 1'}]

@poem.route('/')
def index():
    return render_template('poem_view.html')


# Create a route for the home page
@poem.route('/poem/<int:id>')
def poem_view(id):
    return render_template('poem_view.html', poem=poems[id])
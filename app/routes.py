from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kermit'}
    posts = [
        {
            'author': {'username': 'Scooby'},
            'body': 'Scooby Snacks are the best'
        },
        {
            'author': {'username': 'Shaggy'},
            'body': 'Ghosts are not cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

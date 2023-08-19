from flask import Flask, redirect, render_template
from src.foods import Foods


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/home')


@app.route('/home')
def home():
    PAGE_TITLE = 'Comidas favoritas'
    return render_template('index.html', page_title=PAGE_TITLE)


@app.route('/api', methods=['GET'])
def api():
    foods = Foods.get_favorites()
    return foods

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/players')
def players():
    # Logic to fetch player data and pass it to the template
    return render_template('players.html')

@app.route('/recommendations')
def recommendations():
    # Logic to provide FPL card recommendations
    return render_template('recommendations.html')

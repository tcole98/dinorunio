from app import app
from flask import send_file, render_template

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/leaderboard')
def lead():
    return send_file('leaderboard.html')

@app.route('/app/index.css')
def css():
    return send_file('index.css')
@app.route('/app/index.js')
def js():
    return send_file('index.js')
@app.route('/app/otherstuff.js')
def otherstuff():
    return send_file('otherstuff.js')

@app.route('/assets/default_100_percent/100-offline-sprite.png')
def sprite():
    return send_file('100-offline-sprite.png')

@app.route('/assets/default_100_percent/200-offline-sprite.png')
def sprite2():
    return send_file('200-offline-sprite.png')

@app.route('/app/favicon.ico')
def favicon():
    return send_file('favicon.ico')




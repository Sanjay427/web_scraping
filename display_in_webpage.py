# !/usr/bin/env python3
from flask import Flask, render_template
from nba import get_player_info
from user_database import Database

app = Flask(__name__)


@app.route('/')
def display_image():
    player_info = get_player_info()
    return render_template('index.html', player_info=player_info)


@app.route('/show')
def display_using_database():
    database = Database()
    result = database.select_from_database()
    return render_template('using_database.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

from robopolyapi import app
from flask import send_from_directory
from flask import url_for
from flask import request
from flask import render_template
import os

import sys
import json
import subprocess
import tsol

# TODO: replace this with a static template
@app.route("/")
def hello():
    language = "Python v" + ".".join( [str(x) for x in sys.version_info[0:3]] )
    with app.test_request_context():
        people_link = url_for('get_name', sciper='190000')
        tsol_link = url_for('get_times', arret='EPFL', sens='R')
        music_link = url_for('now_playing')
    return render_template('index.html', framework='Flask',
            language=language, people_link=people_link, tsol_link=tsol_link,
            music_link=music_link)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/people/<int:sciper>")
def get_name(sciper):
    # can't get ldap to compile with python 2.7, please don't hate me for this.
    try:
        output = subprocess.Popen(["python", "/var/www/api/search.py",str(sciper)],stdout=subprocess.PIPE)
        name = output.stdout.readlines()[0].rstrip()
    except:
        name = "Error : No user"
    return  name

# TODO : implement this
@app.route("/camipro/<camipro>")
def get_sciper(camipro):
    '''
    Maps CAMIPRO numbers to SCIPER numbers.

    Used to find a user's unique identifier from his card number
    '''
    return "[not implemented] Return SCIPER #"

@app.route("/music/")
@app.route("/music/<action>", methods=['GET','POST'])
def now_playing(action="playing"):
    '''
    Provides an interface to MPD

    By default, returns currently playing song. POST requests allow some
    control of the music, such as "next, previous, pause, play, stop".
    '''
    if request.method == 'GET':
        result = music_now_playing()
    else:
        result = music_action(action)
    return result

def music_now_playing():
    return "Rick Astley - Never Gonna Give You Up"

def music_action(action="playing"):
    if action == "playing":
        return music_now_playing()
    elif action == "next":
        return "Skipping track."
    elif action == "pause":
        return "Play/Pause"
    elif action == "stop":
        return "Stopped music"
    elif action == "play":
        return "Starting playback"
    elif action == "previous":
        return "Starting playback of previous track"
    else:
        return "Wrong method call"
        

#Ohhhh ouiiii
@app.route("/tsol/")
@app.route("/tsol/<arret>/")
@app.route("/tsol/<arret>/<sens>")
def get_times(arret="EPFL", sens="R"):
    output = tsol.tsol(arret, sens)
    return json.dumps(output)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

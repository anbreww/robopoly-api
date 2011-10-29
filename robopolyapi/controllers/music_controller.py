from robopolyapi import app
from flask import request

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
        

from robopolyapi import app
from flask import request

try:
    import mpd
except ImportError:
    mpd = False

@app.route("/music/")
@app.route("/music/<action>", methods=['GET','POST'])
@app.route("/music/playing/<field>")
def now_playing(action="playing", field="info"):
    '''
    Provides an interface to MPD

    By default, returns currently playing song. POST requests allow some
    control of the music, such as "next, previous, pause, play, stop".
    '''
    if request.method == 'GET':
        result = music_now_playing(field)
    else:
        result = music_action(action)
    return result

def music_now_playing(field):
    if not mpd:
        return "[MPD Module not installed] - The GAME"
    song = get_currentsong()
    fields = ['album', 'composer', 'artist', 'track', 'title', 'pos','time',
            'genre', 'albumartist']
    if field in fields:
        data = song[field]
    if field == "info":
        data = song['artist'] + " - " + song['title']
    if field == "time":
        data = get_timestring(mpdclient.status()['time'])
    return data

def music_action(action="playing"):
    actions = ['playing', 'next', 'skip', 'pause', 'stop', 'play',
               'previous', 'back', 'blah']
    if not action in actions:
        return "Error : that action is not available", 404
    if not mpd:
        return "[MPD Module not installed] - Derp", 404

    c = get_mpdclient()

    if action == "playing":
        response =  music_now_playing()
    elif action == "next" or action == "skip":
        c.next()
        data =  "Skipping track."
    elif action == "pause":
        c.pause()
        data =  "Play/Pause"
    elif action == "stop":
        c.stop()
        data = "Stopped music"
    elif action == "play":
        c.play()
        data = "Starting playback"
    elif action == "previous" or action == "back":
        c.previous()
        data = "Starting playback of previous track"
    else:
        data = ("Error : Method not implemented", 404)

    c.close()
    c.disconnect()

    return data

        
# Helpers
def get_mpdclient():
    mpdclient = mpd.MPDClient()
    mpdclient.connect('localhost',6600)
    return mpdclient

def get_currentsong():
    mpdclient = get_mpdclient()
    song = mpdclient.currentsong()
    mpdclient.close()
    mpdclient.disconnect()
    return song

def sec_to_hms(s):
        '''convert seconds to h:mm:ss format. accepts str and number types'''
        s = int(s)
        h = s/3600
        s -= 3600*h
        m = s/60
        s -= 60*m
        if h > 0:
            return "%d:%02d:%02d" % (h, m, s)
        else:
            return "%d:%02d" % (m,s)

def get_timestring(t):
        '''Elapsed/Total time of current track '''
        t = t.split(":")
        timestat = "{0} / {1}".format(sec_to_hms(t[0]), sec_to_hms(t[1]))
        return timestat

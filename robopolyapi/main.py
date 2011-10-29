from robopolyapi import app
from flask import send_from_directory
from flask import url_for
from flask import render_template
import os

import sys

# TODO: replace this with a static template
@app.route("/")
def hello():
    language = "Python v" + ".".join( [str(x) for x in sys.version_info[0:3]] )
    with app.test_request_context():
        people_link = url_for('get_name', sciper='190000')
        tsol_link = url_for('get_times', arret='EPFL', sens='R')
        music_link = url_for('now_playing')
        camipro_link = url_for('get_sciper', camipro='E9823498123423')
        blah_link = url_for('blah')
    examples=[(people_link, 'The People API'),
                (tsol_link, 'The TSOL API'),
                (music_link, 'The Music API'),
                (blah_link, 'The Blah Page'),
                (camipro_link, 'The Camipro API')]
    return render_template('index.html', framework='Flask',
            language=language, examples=examples)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

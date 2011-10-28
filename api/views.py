from api import app
from flask import send_from_directory
import os

import sys
import json
import subprocess
import tsol

@app.route("/")
def hello():
    return ".".join( [str(x) for x in sys.version_info[0:3]] )

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/people/<int:sciper>")
def get_name(sciper):
    # can't get ldap to compile with python 2.7, please don't hate me for this.
    output = subprocess.Popen(["python", "/var/www/api/search.py",str(sciper)],stdout=subprocess.PIPE)
    name = output.stdout.readlines()[0].rstrip()
    return  name

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

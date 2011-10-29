from flask import Module
from robopolyapi import app

import sys
sys.path.insert(0,'/data/programming/python/api')

from robopolyapi.helpers import tsol
import json

#Ohhhh ouiiii
@app.route("/tsol/")
@app.route("/tsol/<arret>/")
@app.route("/tsol/<arret>/<sens>")
def get_times(arret="EPFL", sens="R"):
    output = tsol.tsol(arret, sens)
    return json.dumps(output)

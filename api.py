from flask import Flask
import sys
import json
import subprocess
import tsol
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
		return ".".join( [str(x) for x in sys.version_info] )

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
#		return tsol(arret, sens)
		output = tsol.tsol(arret, sens)
		return json.dumps(output)

if __name__ == "__main__":
		app.debug = True
		app.run()

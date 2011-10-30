from robopolyapi import app
import subprocess

@app.route("/people/<int:sciper>")
@app.route("/people/<int:sciper>/name")
def get_name(sciper):
    # can't get ldap to compile with python 2.7, please don't hate me for this.
    try:
        output = subprocess.Popen(["python", "/var/www/api/search.py",str(sciper)],stdout=subprocess.PIPE)
        name = output.stdout.readlines()[0].rstrip()
    except:
        name = "Error : No user"
    return  name

@app.route("/people/<int:sciper>/<attribute>")
def get_attribute(sciper, attribute="name"):
    try:
        output = subprocess.Popen(["python", "/data/programming/python/api/robopolyapi/helpers/search.py",str(sciper)],stdout=subprocess.PIPE)
        name = output.stdout.readlines()[0].rstrip()
    except:
        name = "Error : No user"
    return  name


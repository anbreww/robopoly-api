from flask import g, Module, render_template
from robopolyapi import app

@app.route("/blah")
def blah():
    return render_template('blah.html')

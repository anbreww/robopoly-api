from robopolyapi import app
#from flask import current_app

@app.route("/test")
def test():
    return "Testing hello"


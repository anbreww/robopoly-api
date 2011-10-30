from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

from datetime import datetime

import string, random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#app.config['SQLALCHEMY_DATABASE_URI'] =
        #'mysql://username:pass@localhost/username?unix_socket=/usr/local/mysql.sock'

db = SQLAlchemy(app)

class Person(db.Model):

    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    camipro = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    displayname = db.Column(db.String(120))


    def __init__(self, camipro, email):
        self.camipro = camipro
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.camipro

class Transaction(db.Model):

    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person',
            backref=db.backref('transactions', lazy='dymamic'))

    def __init__(self, amount, person, date=None):
        self.amount = amount
        self.person = person
        if date is None:
            date = datetime.utcnow()
        self.date = date

    def __repr__(self):
        return '<Transaction %r>' % self.amount

class Machine(db.Model):

    __tablename__ = "machine"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    apikey = db.Column(db.String(50), unique=True)

    def __init__(self, name, apikey=None):
        self.name = name
        # generate a random machine key
        if apikey is None:
            apikey = ''.join(random.choice(string.ascii_letters +
                string.digits) for x in range(20))
        self.apikey = apikey
        #self.machinetype = blah
        #self.machinegroup = blah
        

import robopolyapi.main
import robopolyapi.test

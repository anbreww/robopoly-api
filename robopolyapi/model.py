from elixir import *

from datetime import datetime
import string, random

metadata.bind = "sqlite:////tmp/elix.db"
metadata.bind.echo = True

setup_all(True)

class Person(Entity):
    camipro = Field(String(30))
    email = Field(String(120))
    name = Field(Unicode(120)) # TODO : replace firstname with name
    firstname = Field(Unicode(120))
    lastname = Field(Unicode(120))
    displayname = Field(Unicode(120))

    transactions = OneToMany('Transaction')
    groups = ManyToMany('PersonGroup')

    def __repr__(self):
        return "<User %s (%s)>" % (self.camipro, self.email)

class Transaction(Entity):
    amount = Field(Integer)
    date = Field(DateTime)

    person = ManyToOne('Person')

    # date must default to datetime.utcnow()
    def __init__(self, amount, date=None, person=None):
        self.amount = amount
        if date is None:
            date = datetime.utcnow()
        self.date = date
        person = person

    def __repr__(self):
        return '<Transaction %r>' % self.amount

class Machine(Entity):
    name = Field(String(120))
    apikey = Field(String(60))

    # Machines can have a "type" attribute
    machinetype = ManyToOne('MachineType')

    # But can belong to several permission groups
    machinegroups = ManyToMany('MachineGroup')

    def __init__(self, name, apikey=None):
        self.name = name
        if apikey is None:
            apikey = ''.join(random.choice(string.ascii_letters +
                string.digits) for x in range(20))
        self.apikey = apikey

    def __repr__(self):
        return '<Machine %r (key: %s)>' % (self.name, self.apikey)

class MachineType(Entity):
    name = Field(String(120))

    machines = OneToMany('Machine')

    def __repr__(self):
        return '<MachineType %r>' % self.name

class PersonGroup(Entity):
    name = Field(String(120))

    # Each person can be part of several groups
    members = ManyToMany('Person')

    # Each group of people can use several groups of machines
    machinegroups = ManyToMany('MachineGroup')

    def __repr__(self):
        return '<PersonGroup %r>' % self.name

class MachineGroup(Entity):
    name = Field(String(120))

    # Each machine can be part of several groups
    machines = ManyToMany('Machine')

    # Each group of machines can be used by several groups of people
    usergroups = ManyToMany('PersonGroup')
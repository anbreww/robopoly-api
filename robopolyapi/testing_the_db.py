# coding: utf-8

'''
Testing the DB.
This file is meant to be run in iPython to set up some data to be tested.
It will create two users, two groups, and three machines.
If all goes well, andrew is part of "members" and "committee", and has access
to all the machines.
User douglas is only part of "members" and therefore can only access nespresso,
the coffee machine.

I have not yet had time to implement the function to test if a user is
allowed to use a machine. It should take two arguments (user and machine)
and return True or False
'''

from model import *

# avoid polluting the screen with SQL
metadata.bind.echo = False

# setup the db for the interactive session
setup_all(True)

# create some member groups
members = PersonGroup(name="Membres")
committee = PersonGroup(name="Comité")


# create some machine groups
coffeemachines = MachineGroup(name="Machines à Café")
cupboards = MachineGroup(name="Armoires")

# set up permissions accordingly
coffeemachines.usergroups.append(members)
coffeemachines.usergroups.append(committee)
cupboards.usergroups.append(committee)

# create a couple of users
andrew = Person(camipro="170951", email="andy@watsons.ch",
        name="Andrew", firstname="Andrew", lastname="Watson",
        displayname="Andrew Watson")
douglas = Person(camipro="180001", email="doug@watsons.ch",
        name="Douglas",firstname="Douglas", lastname="Watson",
        displayname="Douglas Watson")

# add users to appropriate groups
committee.members.append(andrew)
members.members.append(andrew)
members.members.append(douglas)

# create some machines!
leni = Machine(name="LENI")
rouge = Machine(name="Armoire Rouge")
nespresso = Machine(name="Machine Nespresso")

# add those machines to the relevant groups
cupboards.machines.append(leni)
cupboards.machines.append(rouge)
coffeemachines.machines.append(nespresso)


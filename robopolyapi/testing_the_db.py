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
members = PersonGroup(name=u'Membres')
mechies = PersonGroup(name=u'Mécanos') # ont suivi la formation pour machines
committee = PersonGroup(name=u'Comité')


# create some machine groups
coffeemachines = MachineGroup(name=u'Machines à Café')
cupboards = MachineGroup(name=u'Armoires')
powertools = MachineGroup(name=u'Machines-Outils')

# set up permissions accordingly
coffeemachines.usergroups.append(members)
coffeemachines.usergroups.append(committee)
cupboards.usergroups.append(committee)
powertools.usergroups.append(mechies)
powertools.usergroups.append(committee)

# create a couple of users
andrew = Person(camipro="170951", email="andy@watsons.ch",
        name="Andrew", firstname="Andrew", lastname="Watson",
        displayname="Andrew Watson")
douglas = Person(camipro="180001", email="doug@watsons.ch",
        name="Douglas",firstname="Douglas", lastname="Watson",
        displayname="Douglas Watson")
damien = Person(camipro="211819", email="ddrix@epfl.ch",
        name="Damien", firstname="Damien", lastname="Drix",
        displayname="Damien Drix")
louis = Person(camipro="185889", email="louis@derp.ch",
        name="Louis", firstname="Louis", lastname="Masson",
        displayname="Louis Masson")

# complete list of members at robopoly, for later (LDAP) tests
member_numbers = [
        211819, 218273, 174710, 216804, 204926, 213804, 214524, 214789,
        194171, 208372, 202285, 213691, 202964, 184930, 204294, 217327,
        212948, 195865, 187410, 185002, 217532, 211366, 216917, 214013,
        216254, 217384, 217215, 217393, 204893, 189486, 213664, 215720,
        214545, 203964, 211079, 217029, 217237, 215729, 204253, 201867,
        204222, 173889, 217137, 216450, 202916, 185854, 217628, 189769,
        205876, 212326, 202543, 194192, 187795, 206501, 185911, 193112,
        202855, 217589, 216507, 214313, 205507, 213106, 205736, 216063,
        189517, 205221, 212565, 201892, 208425, 217246, 195824, 186020,
        208402, 212620, 214053, 179436, 106628, 201309, 214101, 178369,
        212582, 213109, 217314, 218584, 186848, 201610, 193835, 212440,
        215758, 204115, 178289, 205353, 202647, 205628, 205772, 175019
        ]

committee_numbers = [
        170590, 170951, 175659, 175673, 178296, 178481, 185184, 185880,
        185889, 185952, 186478, 186618, 187754, 192576, 193114, 193939,
        194131
        ]

from helpers.search import SciperSearch
ss = SciperSearch()

def add_from_ldap(sciper, group):
    '''
    Quick helper script to add someone to a given group and the database
    '''
    details = ss.get_tuple(sciper)
    morf = ss.morf(sciper)
    if details is not None:
        # unpack
        sciper, firstname, lastname, displayname, email = details
        firstname = unicode_me(firstname)
        lastname = unicode_me(lastname)
        displayname = unicode_me(displayname)
        user = Person(camipro=sciper, email=email, name=firstname,
                firstname=firstname, lastname=lastname, displayname=displayname)
        if morf == "Male":
            morf = 'm'
        elif morf == 'Female':
            morf = 'f'
        else:
            morf = 'u'

        print group.name + " -> " + displayname + " ( " + sciper + " ) "
        group.members.append(user)
    else:
        print "ERROR : details for # " + str(sciper) + " could not be found."

def unicode_me(a_string):
    return a_string.decode('utf-8')

for userid in member_numbers:
    add_from_ldap(userid, members)

for userid in committee_numbers:
    add_from_ldap(userid, committee)


# add users to appropriate groups
committee.members.append(andrew)
members.members.append(douglas)

# create some machines!
leni = Machine(name="LENI")
rouge = Machine(name="Armoire Rouge")
nespresso = Machine(name="Machine Nespresso")

# add those machines to the relevant groups
cupboards.machines.append(leni)
cupboards.machines.append(rouge)
coffeemachines.machines.append(nespresso)


from fabric.api import *

# user for remote commands : we need to create a user for deployment!
env.user = 'root'

# servers where we want the commands executed
env.hosts = ['dev.robopoly.ch']

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def host_type():
    run('uname -s')

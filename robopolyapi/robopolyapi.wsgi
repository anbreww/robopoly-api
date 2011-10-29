import sys
sys.path.insert(0,"/var/www/api")
sys.path.insert(0,"/var/www/dev")

from robopolyapi import app as application

from robopolyapi.controllers import test_controller
from robopolyapi.controllers import tsol_controller
from robopolyapi.controllers import camipro_controller
from robopolyapi.controllers import people_controller
from robopolyapi.controllers import music_controller

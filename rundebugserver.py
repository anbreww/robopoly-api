from robopolyapi import app

from robopolyapi.controllers import test_controller
from robopolyapi.controllers import tsol_controller
from robopolyapi.controllers import camipro_controller
from robopolyapi.controllers import people_controller
from robopolyapi.controllers import music_controller
    
app.debug = True
app.run(host='0.0.0.0')

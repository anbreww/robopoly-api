from flask import Flask

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#app.config['SQLALCHEMY_DATABASE_URI'] =
        #'mysql://username:pass@localhost/username?unix_socket=/usr/local/mysql.sock'

metadata.bind = "sqlite:////tmp/elix.db"
metadata.bind.echo = True

setup_all(True)

#db = SQLAlchemy(app)

import robopolyapi.main
import robopolyapi.test

import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

from deviceNanny.config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'deviceNanny.sqlite')
    )
    app.config.from_object(Config)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/devicenanny.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Device Nanny startup')

    from . import db
    db.init_app(app)

    # Home page
    from . import home
    app.register_blueprint(home.bp)

    # Add user page
    from . import user
    app.register_blueprint(user.bp)

    # Add devices page
    from . import devices
    app.register_blueprint(devices.bp)

    # Add api endpoint
    from . import api
    app.register_blueprint(api.bp)

    return app

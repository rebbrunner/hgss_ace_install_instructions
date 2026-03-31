import os

from flask import Flask

def factory(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path, 'data.sqlite')
    )

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)
    
    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    db.init_app(app)

    from . import base
    app.register_blueprint(base.bp)

    return app

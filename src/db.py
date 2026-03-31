import sqlite3 as sql
from datetime import datetime

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sql.connect(
            current_app.config['DATABASE'],
            detect_types=sql.PARSE_DECLTYPES
        )
        g.db.row_factory = sql.Row
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('models.sql') as f:
        db.executescript(f.read().deocde('utf8'))

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized database')

sql.register_converter(
    'timestamp', lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

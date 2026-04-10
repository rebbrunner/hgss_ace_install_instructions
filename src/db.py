import os

import sqlite3 as sql
import psycopg2
import psycopg2.extras
from datetime import datetime

import click
from flask import current_app, g

def get_db():
    DB_URL = os.environ.get('DB_URL')

    if 'db' not in g:
        if not DB_URL:
            g.db = sql.connect(
                current_app.config['DATABASE'],
                detect_types=sql.PARSE_DECLTYPES
            )
            g.db.row_factory = sql.Row
        else:
            g.db = psycopg2.connect(DB_URL)
            g.db.cursor_factory=psycopg2.extras.RealDictCursor
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    DB_URL = os.environ.get('DB_URL')

    db = get_db()
    with current_app.open_resource('models.sql') as f:
        if not DB_URL:
            db.executescript(f.read().decode('utf8'))
        else:
            script = f.read()
            with db.cursor() as cur:
                cur.execute(script)
            db.commit()

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized database')

if not os.environ.get("DB_URL"):  # only for SQLite
    sql.register_converter(
        'timestamp', lambda v: datetime.fromisoformat(v.decode())
    )

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

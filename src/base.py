from flask import Blueprint, render_template
from src.db import get_db

bp = Blueprint('base', __name__, url_prefix='/')

@bp.route('/')
def index():
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM documentation WHERE title = %s',('introduction',))
    main_section=cur.fetchone()

    if main_section:
        cur.execute('SELECT * FROM documentation WHERE pid=%s',(main_section['id'],))
        child_sections = cur.fetchall()
    else:
        child_sections = []
    return render_template('index.html', main_section=main_section, child_sections=child_sections)

from flask import Blueprint, render_template
from src.db import get_db

bp = Blueprint('base', __name__, url_prefix='/')

@bp.route('/')
def index():
    db = get_db()
    main_section = db.execute('SELECT * FROM documentation WHERE title = ?',('introduction',)).fetchone()
    child_sections = db.execute('SELECT * FROM documentation WHERE pid=?',(main_section['id'],))
    return render_template('index.html', main_section=main_section, child_sections=child_sections)

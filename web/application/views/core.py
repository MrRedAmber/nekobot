from flask import Blueprint, render_template


core = Blueprint('core', __name__)


@core.route('/')
def core_get_index():
    return render_template('index.html')

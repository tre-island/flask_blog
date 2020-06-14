from flask import Blueprint, Flask, flash, render_template

app = Flask(__name__)

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    return render_template('home.html', title="Home Page")
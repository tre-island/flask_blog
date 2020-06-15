from flask import Blueprint, Flask, flash, render_template

app = Flask(__name__)

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    summary = """
    We’ll likely have to wait until Sony gives official dimensions (or shows the physical box next to something else 
    for scale) of the controversial design to know for sure, but that isn’t stopping fans on the internet from doing their 
    best to estimate things. And based on early guesses, the PS5 is going to be huge — perhaps even the 
    biggest mainstream console in years.
    """

    feature = {
        "title": "The PS5 is huge, according to internet detectives",
        "summary": f'{summary[:200]} ...'
    }
    return render_template('blog/index.html', title="My Blog Page", feature=feature)
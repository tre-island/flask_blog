from flask import Blueprint, Flask, flash, render_template

app = Flask(__name__)

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    summary = """
    Sony has finally shown off what the PlayStation 5 will look like, but there’s one very big question about the design
    that’s still unclear: just how big is the PlayStation 5?
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
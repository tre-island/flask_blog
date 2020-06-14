from flask import Blueprint, Flask, render_template

from flask_blog import blog

app = Flask(__name__)


def create_app():
    app.register_blueprint(blog.bp)


create_app()

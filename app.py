
if __name__ == "__main__":

    from flask import Flask

    from flask_blog import blog

    app = Flask(__name__, template_folder='flask_blog/templates', )

    app.register_blueprint(blog.bp)

    app.run(debug=True, host="0.0.0.0")

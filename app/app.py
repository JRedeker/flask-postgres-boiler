from database import db
from flask import Flask
from module_one.views import module_one
from module_two.views import module_two


def create_app():
    # create the application object and configure
    app = Flask(__name__)
    app.config.from_pyfile('configure.py')
    with app.app_context():
        db.init_app(app)
        app.register_blueprint(module_one, url_prefix='')
        app.register_blueprint(module_two, url_prefix='')
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()
        db.session.commit()


# Create app, setup db, and run app
if __name__ == "__main__":
    app = create_app()
    setup_database(app)
    app.run(host='0.0.0.0')

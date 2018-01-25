# IMPORTS
import psycopg2
import yaml

from flask import Flask, render_template

# APP CONFIG
app = Flask(__name__)
app.config.from_pyfile('configure.py')

config_file = open("config.yml", "r")
config = yaml.load(config_file)
db = config['database_cfg']


# CONTROLLERS
@app.route("/")
def hello():
    return "App running"


@app.route("/dbtest")
def dbtest():

    try:

        connection = psycopg2.connect(**db)
        cursor = connection.cursor()

        cursor.execute("""SELECT * FROM {}""".format(config['tables']['main']))

        connection.close()

        return "Database connected"

    except:

        return "Database not connected!"


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


# 🚀 LAUNCH  🚀


if __name__ == "__main__":

    app.run(host='0.0.0.0')

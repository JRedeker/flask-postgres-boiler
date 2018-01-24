# IMPORTS


from flask import Flask, render_template
import psycopg2
import yaml


# APP CONFIG


app = Flask(__name__)
app.config.from_pyfile('configure.py')

config_file = open("config.yml", "r")
config = yaml.load(config_file)
db = config['database_cfg']

connection = psycopg2.connect(**db)
cursor = connection.cursor()

# CONTROLLERS


@app.route("/")
def hello():
    try:
        cursor.execute("""SELECT * FROM {}""".format(config['tables']['main']))
        return "Database connected"
    except:
        return "Database not connected!"


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    app.run()

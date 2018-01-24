import psycopg2
import yaml

from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('configure.py')

config_file = open("config.yml", "r")
config = yaml.load(config_file)
db = config['database_cfg']


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


if __name__ == "__main__":

    app.run(host='0.0.0.0')

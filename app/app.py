from flask import Flask
import psycopg2
import yaml

app = Flask(__name__)
app.config.from_pyfile('configure.py')

config_file = open("config.yml", "r")
config = yaml.load(config_file)
db = config['database_cfg']

connection = psycopg2.connect(**db)
cursor = connection.cursor()


@app.route("/")
def hello():
    try:
        cursor.execute("""SELECT * FROM {}""".format(config['tables']['main']))
        return "Database connected"
    except:
        return "Database not connected!"


if __name__ == "__main__":
    app.run()

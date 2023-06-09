import flask
import gunicorn
import scipy
from lib.example import shared
from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route("/")
def root():
    return {
        "flask": flask.__version__,
        "gunciorn": gunicorn.__version__,
        "scipy": scipy.__version__,
        "shared (requests)": shared(),
        "psycopg2": psycopg2.__version__,
    }


if __name__ == "__main__":
    app.run(debug=True)

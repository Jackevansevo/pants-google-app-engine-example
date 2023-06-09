import flask
import gunicorn
import scipy
from lib.example import shared
from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return {
        "flask": flask.__version__,
        "gunciorn": gunicorn.__version__,
        "scipy": scipy.__version__,
        "shared (requests)": shared(),
    }


if __name__ == "__main__":
    app.run(debug=True)

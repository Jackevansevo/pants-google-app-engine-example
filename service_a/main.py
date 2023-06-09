import flask
import gunicorn
import scipy
from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return {
        "flask": flask.__version__,
        "gunciorn": gunicorn.__version__,
        "scipy": scipy.__version__,
    }


if __name__ == "__main__":
    app.run(debug=True)

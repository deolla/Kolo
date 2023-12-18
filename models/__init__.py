from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from helper_func import get_secret_key


app = Flask(__name__, template_folder="../templates", static_folder="../static") # Flask app instance.
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///kolo.db' # Database URI.
app.config["SECRET_KEY"] = get_secret_key() # Secret key for configuration.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)

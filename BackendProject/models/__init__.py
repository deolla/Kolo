from flask import Flask
import os
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from helper_func import get_secret_key
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__, template_folder="../templates", static_folder="../static") # Flask app instance.
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///kolo.db' # Database URI.
app.config["SECRET_KEY"] = get_secret_key() # Secret key for configuration.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = get_secret_key()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "deosundeola@gmail.com"
app.config["MAIL_PASSWORD"] = "nkzt nljs seih pvsx"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
# Enable mail debugging for development
app.config["MAIL_DEBUG"] = True
app.config["MAIL_DEFAULT_SENDER"] = "adeolaesther761@gmail.com"

db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="memory://",
)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

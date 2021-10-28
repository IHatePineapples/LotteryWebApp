# IMPORTS
import socket
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'VeryLongAndVeryRandomNotSoSecretKey'
app.config['RECAPTCHA_PUBLIC_KEY'] = "6LeQO_wcAAAAAGXaY5t9L2W9ro3F_5JSM3uo-fyi"
app.config['RECAPTCHA_PRIVATE_KEY'] = "6LeQO_wcAAAAAAbaqBkIKnBkueYcrnGIZUa-pMyc"


# initialise database
db = SQLAlchemy(app)


# HOME PAGE VIEW
@app.route('/')
def index():
    return render_template('index.html')

# ERROR HANDLERS/PAGE VIEWS
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404
@app.errorhandler(403)
def not_found(e):
    return render_template("403.html"), 403
@app.errorhandler(500)
def not_found(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    my_host = "127.0.0.1"
    free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    free_socket.bind((my_host, 0))
    free_socket.listen(5)
    free_port = free_socket.getsockname()[1]
    free_socket.close()

    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # BLUEPRINTS
    # import blueprints
    from users.views import users_blueprint
    from admin.views import admin_blueprint
    from lottery.views import lottery_blueprint

    # register blueprints with app
    app.register_blueprint(users_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(lottery_blueprint)

    app.run(host=my_host, port=free_port, debug=True)

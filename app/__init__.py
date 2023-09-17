from flask import Flask
import os

from app.controllers.URLs import mod_main
from app.module_role.controllers import mod_role
from app.module_user.controllers import mod_user

app = Flask(__name__)

secret_key = os.urandom(24)

# Register blueprint(s)

app.register_blueprint(mod_main)
app.register_blueprint(mod_role)
app.register_blueprint(mod_user)

app.secret_key = secret_key

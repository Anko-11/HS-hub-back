from flask import Blueprint

user_db = Blueprint("user_bp", __name__, url_prefix="/v1/")

from . import user

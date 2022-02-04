from flask import Blueprint, Flask
from app.routes.posts_route import bp as bp_posts

bp_api = Blueprint("api", __name__, url_prefix="/api")

def init_app(app: Flask):
    bp_api.register_blueprint(bp_posts)
    app.register_blueprint(bp_api)
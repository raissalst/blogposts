from flask import Blueprint
from app.controllers import posts_controller

bp = Blueprint("posts", __name__, url_prefix="/posts")

bp.post("")(posts_controller.create_post)
bp.get("")(posts_controller.read_posts)
bp.get("/<int:post_id>")(posts_controller.read_post_by_id)
bp.patch("/<int:post_id>")(posts_controller.update_post)
bp.delete("/<int:post_id>")(posts_controller.delete_post)
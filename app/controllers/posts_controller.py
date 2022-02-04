from flask import request, jsonify
from app.exc.not_found_error import NotFoundError
from app.models.posts_model import Post
from http import HTTPStatus
import os


def create_post():
    data = request.get_json()

    keys_entered = data.keys()

    wrong_keys = Post.check_keys_received(keys_entered)

    try:
        new_post = Post(**data)
        new_post.new_post()
        Post.serialize_posts(new_post)
        new_post_dict = new_post.__dict__
        del new_post_dict["_id"]
        return jsonify(new_post_dict), HTTPStatus.CREATED
    except TypeError:
        return {"available_keys": os.getenv('VALID_KEYS').split(","), "wrong_keys_sent": wrong_keys}

def read_posts():
    ...


def read_one_post(post_id):
    ...


def update_post(post_id):
    ...


def delete_post(post_id):
    ...
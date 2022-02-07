from flask import request, jsonify
from app.exc.not_found_error import NotFoundError
from app.exc.not_list_type_error import NotListTypeError
from app.models.posts_model import Post
from http import HTTPStatus
import os
from json import loads


def create_post():
    data = request.get_json()

    keys_entered = data.keys()

    wrong_keys = Post.check_keys_received(keys_entered)

    try:
        new_post = Post(**data)
        new_post.new_post()
        new_post_dict = new_post.__dict__
        del new_post_dict["_id"]
        return jsonify(new_post_dict), HTTPStatus.CREATED

    except TypeError:
        return {"available_keys": os.getenv('VALID_KEYS').split(","), "wrong_keys_sent": wrong_keys}, HTTPStatus.BAD_REQUEST

    except NotListTypeError as e:
        return e.message

def read_posts():
    list_of_posts = list(Post.get_posts())

    if len(list_of_posts) == 0:
        empty_table = os.getenv("EMPTY_TABLE_RETURN")
        return empty_table, HTTPStatus.OK

    for item in list_of_posts:
        del item["_id"]

    new_list_of_posts = loads(os.getenv("EMPTY_TABLE_RETURN"))
    new_list_of_posts.get("posts").extend(list_of_posts)

    return jsonify(new_list_of_posts), HTTPStatus.OK


def read_one_post(post_id):
    try:
        post_filtered = Post.filter_post(post_id)
        return jsonify(post_filtered), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


def update_post(post_id):
    data = request.get_json()

    keys_entered = data.keys()
    wrong_keys = Post.check_keys_received(keys_entered)

    if len(wrong_keys) != 0:
        return {"available_keys": os.getenv('VALID_KEYS').split(","), "wrong_keys_sent": wrong_keys}, HTTPStatus.BAD_REQUEST

    try:
        is_post_there = Post.filter_post(post_id)
        new_updated_post = Post.update_post(post_id, data)
        del new_updated_post["_id"]
        return jsonify(new_updated_post), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except NotListTypeError as e:
        return e.message
    

def delete_post(post_id):
    try:
        deleted_post = Post.delete_post(post_id)
        return jsonify(deleted_post), HTTPStatus.OK

    except NotFoundError as e:
        return e.message
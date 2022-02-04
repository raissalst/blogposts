from flask import request, jsonify
from app.exc.not_found_error import NotFoundError
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
        Post.serialize_posts(new_post)
        new_post_dict = new_post.__dict__
        del new_post_dict["_id"]
        return jsonify(new_post_dict), HTTPStatus.CREATED
    except TypeError:
        return {"available_keys": os.getenv('VALID_KEYS').split(","), "wrong_keys_sent": wrong_keys}, HTTPStatus.BAD_REQUEST

def read_posts():
    list_of_posts = list(Post.get_posts())

    if len(list_of_posts) == 0:
        empty_table = os.getenv("EMPTY_TABLE_RETURN")
        return empty_table, HTTPStatus.OK

    Post.serialize_posts(list_of_posts)

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
    ...


def delete_post(post_id):
    ...
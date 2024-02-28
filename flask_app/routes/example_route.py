from flask import Blueprint, jsonify
from models import Example, db

example = Blueprint("Example", __name__)

@example.route("/", methods=["GET"])
def get_home():
    return "Hello World"

@example.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    try:
        example = Example.query.get(id)
    except BaseException as e:
        return jsonify({"message":f"Bad Request: {e}"})
    return example.to_dict()

    
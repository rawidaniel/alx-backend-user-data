#!/usr/bin/env python3
"""
Module app
Basic Flask app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Home route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """Register user
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Authenticate the user using user credential
    """
    email = request.form.get("email")
    password = request.form.get("password")
    session_id = AUTH.create_session(email=email)
    if session_id is None:
        abort(401)
    valid_password = AUTH.valid_login(email, password)
    if not valid_password:
        abort(401)
    response = jsonify({"email": f"email", "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

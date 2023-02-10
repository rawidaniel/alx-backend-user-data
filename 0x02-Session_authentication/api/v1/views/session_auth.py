#!/usr/bin/env python3
"""
Module session_auth
"""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def session_authentication() -> str:
    """handles all routes for the Session authentication
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    valid_password = user[0].is_valid_password(password)
    if not valid_password:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)
    return response

#!/usr/bin/env python3
"""
Module app
Basic Flask app
"""
from flask import Flask, jsonify, request
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
    """
    """
    print("************")
    email = request.form.get("email")
    password = request.form.get("password")
    print(email, password)
    return f"{email} {password}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

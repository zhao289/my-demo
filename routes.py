from flask import jsonify, request
import json
import os
from models import dummy_recommend, check_user, register_user

DATA_PATH = os.path.join(os.path.dirname(__file__), "data")

def setup_routes(app):
    sample_file = os.path.join(DATA_PATH, "sample_data.json")
    users_file = os.path.join(DATA_PATH, "users.json")

    @app.route("/api/reminders")
    def get_reminders():
        with open(sample_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data.get("reminders", []))

    @app.route("/api/neighbor-items")
    def get_neighbor_items():
        with open(sample_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        items = data.get("neighbor_items", [])
        recommended = dummy_recommend(items)
        return jsonify(recommended)

    @app.route("/api/health")
    def get_health():
        with open(sample_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        health = data.get("health", {})
        health["suggestions"] = dummy_recommend(health.get("suggestions", []))
        return jsonify(health)

    # 用户登录
    @app.route("/api/login", methods=["POST"])
    def login():
        data = request.json
        username = data.get("username")
        password = data.get("password")
        if check_user(users_file, username, password):
            return jsonify({"status": "success"})
        return jsonify({"status": "fail"}), 401

    # 用户注册
    @app.route("/api/register", methods=["POST"])
    def register():
        data = request.json
        username = data.get("username")
        password = data.get("password")
        if register_user(users_file, username, password):
            return jsonify({"status": "success"})
        return jsonify({"status": "fail", "message": "用户名已存在"}), 400
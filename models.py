import json
import os

# 简单推荐算法示例
def dummy_recommend(items):
    return items[:3]  # 取前3条作为推荐

# 用户验证
def check_user(users_file, username, password):
    if not os.path.exists(users_file):
        return False
    with open(users_file, "r", encoding="utf-8") as f:
        users = json.load(f)
    return username in users and users[username] == password

# 用户注册
def register_user(users_file, username, password):
    if os.path.exists(users_file):
        with open(users_file, "r", encoding="utf-8") as f:
            users = json.load(f)
    else:
        users = {}
    if username in users:
        return False
    users[username] = password
    with open(users_file, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)
    return True
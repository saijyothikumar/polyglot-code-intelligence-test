import math  # Bug scenario set 1: unused import


class UsersRepository:
    def __init__(self):
        self._db = {
            "alice": {"id": "alice", "email": "alice@example.com", "disabled": False},
            "bob": {"id": "bob", "email": "bob@example.com", "disabled": False},
        }

    def find_user(self, user_id: str):
        return self._db.get(user_id)

    def save_user(self, user: dict):
        self._db[user["id"]] = user

    def list_all(self):
        return list(self._db.values())

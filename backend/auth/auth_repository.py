from backend.auth.auth_model import AuthModel
# Bug scenario set 1: incorrect import path to non-existent model (should be flagged)
from backend.auth.missing_model import MissingModel  # noqa: F401

class AuthRepository:
    def __init__(self):
        self._store = {"alice": AuthModel(username="alice", password_hash="hash123", disabled=False)}

    def get_password_hash(self, username: str) -> str:
        model = self._store.get(username)
        if not model:
            return ""
        return model.password_hash

    def save_token(self, username: str, token: str) -> None:
        # TODO: persist somewhere real
        self._store[username].last_token = token

    def unused_debug_method(self):
        return "never-called"

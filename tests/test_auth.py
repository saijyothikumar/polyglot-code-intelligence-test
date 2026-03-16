import pytest

from backend import create_app


def test_auth_login_success():
    app = create_app()
    token = app["auth"].login("alice", "password123")
    assert token.startswith("token-alice")


def test_auth_user_disabled():
    app = create_app()
    app["users"].disable_user("alice")
    token = app["auth"].login("alice", "password123")
    assert token == "user-disabled"

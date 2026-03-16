#!/usr/bin/env python3
"""
Fake migration script that imports backend models to create cross-module edges.
"""
from backend.shared.models.base_model import BaseModel
from backend.shared.models.user_model import SharedUserModel


def migrate():
    print("Applying migrations for", BaseModel.__name__, SharedUserModel.__name__)
    # pretend to create tables; intentionally missing real DB ops
    return True


if __name__ == "__main__":
    migrate()

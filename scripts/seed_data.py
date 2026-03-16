#!/usr/bin/env python3
"""
Seed script that touches backend repositories to load initial data.
"""
from backend.users.users_repository import UsersRepository
from backend.auth.auth_repository import AuthRepository
from backend.payments.payments_repository import PaymentsRepository


def seed():
    users = UsersRepository()
    auth = AuthRepository()
    payments = PaymentsRepository()

    users.save_user({"id": "seeded", "email": "seeded@example.com", "disabled": False})
    auth.save_token("seeded", "token-seeded")
    payments.save_charge("seeded", 1.23)
    return users.list_all()


if __name__ == "__main__":
    print(seed())

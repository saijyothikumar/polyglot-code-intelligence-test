"""
App bootstrapping module.
Intentionally minimal to let code-intel tools walk the dependency graph.
"""
from backend import create_app

# expose a singleton for convenience; real apps should avoid globals
app = create_app()

def demo_flow():
    auth = app["auth"]
    users = app["users"]
    payments = app["payments"]

    token = auth.login("alice", "password123")
    charge = payments.charge("alice", 42.00)
    profile = users.get_profile("alice")
    return {"token": token, "charge": charge, "profile": profile}

if __name__ == "__main__":
    result = demo_flow()
    print("demo result", result)

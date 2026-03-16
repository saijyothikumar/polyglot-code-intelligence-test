import random
import os
from datetime import datetime
import importlib


def generate_trace_id() -> str:
    return f"trace-{datetime.utcnow().timestamp()}-{random.randint(1000, 9999)}"


def mask_email(email: str) -> str:
    if "@" not in email:
        return email
    name, domain = email.split("@", 1)
    return f"{name[0]}***@{domain}"

# dead helper that nobody calls

def noop_formatter(value):
    return str(value)

# Bug scenario set 3: conditional/dynamic import that may resolve to a missing module
if os.getenv("ENABLE_EXPERIMENTAL") == "1":
    try:
        experimental = importlib.import_module("backend.experiments.experimental_feature")  # noqa: F401
    except ModuleNotFoundError:
        # swallow to keep runtime limping along
        experimental = None

import hashlib

def hash_password(raw: str) -> str:
    # intentionally weak hashing to illustrate security issue
    return hashlib.md5(raw.encode()).hexdigest()

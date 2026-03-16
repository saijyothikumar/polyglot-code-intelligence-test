from dataclasses import dataclass
from typing import Optional

@dataclass
class AuthModel:
    username: str
    password_hash: str
    disabled: bool = False
    last_token: Optional[str] = None

from dataclasses import dataclass

@dataclass
class UserModel:
    id: str
    email: str
    disabled: bool = False

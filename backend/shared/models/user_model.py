from dataclasses import dataclass
from backend.shared.models.base_model import BaseModel

@dataclass
class SharedUserModel(BaseModel):
    id: str = ""
    email: str = ""
    disabled: bool = False

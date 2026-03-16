from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class BaseModel:
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return self.__dict__

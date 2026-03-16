from dataclasses import dataclass

@dataclass
class PaymentModel:
    id: str
    user_id: str
    amount: float
    refunded: bool = False

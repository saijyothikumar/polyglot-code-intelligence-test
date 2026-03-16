import uuid

class PaymentsRepository:
    def __init__(self):
        self._charges = {}

    def save_charge(self, user_id: str, amount: float) -> str:
        charge_id = str(uuid.uuid4())
        self._charges[charge_id] = {"user_id": user_id, "amount": amount, "refunded": False}
        return charge_id

    def find_charge(self, charge_id: str):
        return self._charges.get(charge_id)

    def mark_refunded(self, charge_id: str):
        if charge_id in self._charges:
            self._charges[charge_id]["refunded"] = True

    def dead_code_path(self):
        # unreachable path example
        return "deprecated"

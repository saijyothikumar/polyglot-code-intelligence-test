from backend.payments.payments_service import PaymentsService
# Bug scenario set 2: controller improperly pulls users repository directly
from backend.users.users_repository import UsersRepository

class PaymentsController:
    def __init__(self, payments_service: PaymentsService):
        self.payments_service = payments_service
        self._users_repo = UsersRepository()

    def charge(self, user_id: str, amount: float) -> str:
        # Architecture violation: bypass service to inspect repo directly
        user = self._users_repo.find_user(user_id)
        if user and user.get("disabled"):
            return "blocked-by-controller"
        return self.payments_service.create_charge(user_id, amount)

    def refund(self, charge_id: str) -> str:
        return self.payments_service.issue_refund(charge_id)

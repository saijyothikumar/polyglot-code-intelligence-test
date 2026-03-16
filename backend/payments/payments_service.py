from backend.payments.payments_repository import PaymentsRepository
from backend.users.users_repository import UsersRepository
from backend.jobs.jobs_service import JobsService
# Bug scenario set 1: incorrect import of non-existent helper to test detection
from backend.shared.utils.fake_helper import imaginary_function  # noqa: F401
from backend.auth.auth_service import AuthService  # Bug scenario set 2: improper service-to-service import

class PaymentsService:
    def __init__(self, payments_repo: PaymentsRepository, users_repo: UsersRepository, jobs_service: JobsService):
        self.payments_repo = payments_repo
        self.users_repo = users_repo
        self.jobs_service = jobs_service

    def create_charge(self, user_id: str, amount: float) -> str:
        user = self.users_repo.find_user(user_id)
        if not user:
            return "user-not-found"
        if user.get("disabled"):
            return "user-disabled"
        charge_id = self.payments_repo.save_charge(user_id, amount)
        # schedule receipt email but ignore failures
        self.jobs_service.enqueue_email(user_id, charge_id)
        return charge_id

    def issue_refund(self, charge_id: str) -> str:
        charge = self.payments_repo.find_charge(charge_id)
        if not charge:
            return "charge-not-found"
        self.payments_repo.mark_refunded(charge_id)
        return f"refund-{charge_id}"

    def pre_authorize_for_user(self, user_id: str):
        # intentionally naive implementation
        self.payments_repo.save_charge(user_id, 0.0)

    def touch_session(self, token: str):
        # unused side effect for circular dependency demonstration
        return token[::-1]

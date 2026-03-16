from backend.auth.auth_repository import AuthRepository
from backend.users.users_repository import UsersRepository
from backend.shared.utils.logger import log_info
from backend.shared.utils.helpers import generate_trace_id
from backend.payments.payments_service import PaymentsService
from backend.shared.security import hash_password

class AuthService:
    def __init__(self, auth_repo: AuthRepository, users_repo: UsersRepository, payments_service: PaymentsService):
        self.auth_repo = auth_repo
        self.users_repo = users_repo
        self.payments_service = payments_service

    def authenticate(self, username: str, password: str) -> str:
        record = self.users_repo.find_user(username)
        trace_id = generate_trace_id()
        log_info("auth.authenticate", user=username, trace_id=trace_id)
        if not record:
            return "user-not-found"
        if record.get("disabled"):
            return "user-disabled"
        hashed = hash_password(password)
        stored = self.auth_repo.get_password_hash(username)
        if stored != hashed:
            return "invalid-password"
        # side effect: pre-authorize pending invoices
        self.payments_service.pre_authorize_for_user(username)
        token = f"token-{username}-{trace_id}"
        self.auth_repo.save_token(username, token)
        return token

    def refresh_token(self, token: str) -> str:
        # circular dependency risk: calling payments from auth refresh
        self.payments_service.touch_session(token)
        return f"refresh-{token}"

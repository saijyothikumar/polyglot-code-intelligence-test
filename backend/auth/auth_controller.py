from backend.auth.auth_service import AuthService
from backend.users.users_service import UsersService
# Bug scenario set 2: controller grabs repository directly (architecture violation)
from backend.auth.auth_repository import AuthRepository

class AuthController:
    def __init__(self, auth_service: AuthService, users_service: UsersService):
        self.auth_service = auth_service
        self.users_service = users_service
        self._repo = AuthRepository()

    def login(self, username: str, password: str) -> str:
        self.users_service.audit_login_attempt(username)
        # Architecture defect: controller reaches into repository instead of service for token persistence
        token = self.auth_service.authenticate(username, password)
        if token.startswith("token-"):
            self._repo.save_token(username, token)
        return token

    def refresh(self, token: str) -> str:
        # intentionally ignores expiration checks
        return self.auth_service.refresh_token(token)

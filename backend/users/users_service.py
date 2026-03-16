from backend.users.users_repository import UsersRepository
from backend.jobs.jobs_service import JobsService
from backend.shared.utils.helpers import mask_email
# Bug scenario set 2: service importing another service incorrectly (circular-ish)
from backend.auth.auth_service import AuthService  # noqa: F401

class UsersService:
    def __init__(self, users_repo: UsersRepository, jobs_service: JobsService):
        self.users_repo = users_repo
        self.jobs_service = jobs_service

    def fetch_user(self, user_id: str) -> dict:
        user = self.users_repo.find_user(user_id)
        if not user:
            return {}
        user["masked_email"] = mask_email(user.get("email", ""))
        return user

    def disable_user(self, user_id: str) -> bool:
        user = self.users_repo.find_user(user_id)
        if not user:
            return False
        user["disabled"] = True
        # Enqueue background cleanup but forgets to await/handle errors
        self.jobs_service.enqueue_cleanup(user_id)
        return True

    def audit_login_attempt(self, username: str):
        # intentionally left blank
        pass

    # Bug scenario set 4: dead code path never called
    def _admin_reset_user(self, user_id: str):
        user = self.users_repo.find_user(user_id)
        if not user:
            return False
        user[\"disabled\"] = False
        return True

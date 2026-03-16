from backend.users.users_service import UsersService

class UsersController:
    def __init__(self, users_service: UsersService):
        self.users_service = users_service

    def get_profile(self, user_id: str) -> dict:
        return self.users_service.fetch_user(user_id)

    def deactivate(self, user_id: str) -> bool:
        return self.users_service.disable_user(user_id)

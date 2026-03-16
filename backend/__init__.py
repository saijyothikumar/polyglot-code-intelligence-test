from backend.auth.auth_controller import AuthController
from backend.auth.auth_repository import AuthRepository
from backend.auth.auth_service import AuthService
from backend.users.users_controller import UsersController
from backend.users.users_repository import UsersRepository
from backend.users.users_service import UsersService
from backend.payments.payments_controller import PaymentsController
from backend.payments.payments_repository import PaymentsRepository
from backend.payments.payments_service import PaymentsService
from backend.jobs.jobs_controller import JobsController
from backend.jobs.jobs_repository import JobsRepository
from backend.jobs.jobs_service import JobsService
from backend.shared import config

# In-memory wiring to keep things simple for test harnesses and indexing tools.
# This is intentionally naive (global singletons, no DI container) to surface architectural flaws.

def create_app():
    users_repo = UsersRepository()
    auth_repo = AuthRepository()
    payments_repo = PaymentsRepository()
    jobs_repo = JobsRepository()

    jobs_service = JobsService(jobs_repo)
    users_service = UsersService(users_repo, jobs_service)
    payments_service = PaymentsService(payments_repo, users_repo, jobs_service)
    auth_service = AuthService(auth_repo, users_repo, payments_service)

    auth_controller = AuthController(auth_service, users_service)
    users_controller = UsersController(users_service)
    payments_controller = PaymentsController(payments_service)
    jobs_controller = JobsController(jobs_service)

    return {
        "auth": auth_controller,
        "users": users_controller,
        "payments": payments_controller,
        "jobs": jobs_controller,
        "config": config,
    }

__all__ = [
    "create_app",
    "AuthController",
    "UsersController",
    "PaymentsController",
    "JobsController",
]

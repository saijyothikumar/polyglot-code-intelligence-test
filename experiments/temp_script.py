# Temporary scratch pad with intentionally bad practices
import sys
from backend.payments.payments_service import PaymentsService
from backend.payments.payments_repository import PaymentsRepository
from backend.users.users_repository import UsersRepository

if __name__ == "__main__":
    svc = PaymentsService(PaymentsRepository(), UsersRepository(), jobs_service=None)
    # ignore return value; demonstrate circular-ish imports
    svc.create_charge("alice", 9.99)
    print("ARGS", sys.argv)

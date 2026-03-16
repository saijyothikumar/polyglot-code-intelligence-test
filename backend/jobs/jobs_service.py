from backend.jobs.jobs_repository import JobsRepository

class JobsService:
    def __init__(self, jobs_repo: JobsRepository):
        self.jobs_repo = jobs_repo

    def enqueue_cleanup(self, user_id: str):
        return self.jobs_repo.enqueue_job("cleanup", {"user_id": user_id})

    def enqueue_email(self, user_id: str, charge_id: str):
        return self.jobs_repo.enqueue_job("email", {"user_id": user_id, "charge_id": charge_id})

    def execute(self, name: str):
        job = self.jobs_repo.dequeue_job(name)
        if not job:
            return "no-job"
        return f"executed-{name}"

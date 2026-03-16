from backend.jobs.jobs_service import JobsService

class JobsController:
    def __init__(self, jobs_service: JobsService):
        self.jobs_service = jobs_service

    def run(self, name: str):
        return self.jobs_service.execute(name)

"""
Messy job scraper that mixes requests-like pseudocode with filesystem writes.
"""
import random
from pathlib import Path
from backend.jobs.jobs_repository import JobsRepository
from backend.shared.utils.logger import log_info

try:
    import requests  # noqa: F401
except ImportError:
    requests = None  # pseudo optional dependency


def scrape_jobs():
    repo = JobsRepository()
    for i in range(3):
        repo.enqueue_job("scrape", {"page": i, "seed": random.random()})
    log_info("scrape_jobs", queued=len(repo.queue))
    Path("experiments/jobs_dump.txt").write_text(str(repo.queue))


if __name__ == "__main__":
    scrape_jobs()

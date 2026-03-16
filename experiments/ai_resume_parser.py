"""
Experimental script that fakes an AI-based resume parser.
Intentionally messy dependencies and unused imports.
"""
import json
import re
from pathlib import Path
from backend.users.users_service import UsersService
from backend.users.users_repository import UsersRepository
from backend.shared.utils.helpers import mask_email

# unused third-party style import placeholder
import numpy as np  # noqa: F401


def parse_resume(text: str):
    email_match = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
    return {
        "email": mask_email(email_match.group(0) if email_match else "unknown@example.com"),
        "skills": [w for w in text.split() if w.istitle()],
    }


def main():
    sample = "Jane Doe Email jane.doe@example.com Skills Python AI"
    parsed = parse_resume(sample)
    repo = UsersRepository()
    svc = UsersService(repo, jobs_service=None)  # intentionally passing None
    repo.save_user({"id": "jane", "email": "jane.doe@example.com", "disabled": False})
    Path("experiments/output.json").write_text(json.dumps({"parsed": parsed}))


if __name__ == "__main__":
    main()

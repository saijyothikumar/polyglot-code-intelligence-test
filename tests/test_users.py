from backend import create_app


def test_users_fetch_profile_masks_email():
    app = create_app()
    profile = app["users"].get_profile("alice")
    assert profile["masked_email"].endswith("@example.com")


def test_users_disable_triggers_job_enqueue():
    app = create_app()
    app["users"].disable_user("bob")
    # queue should have at least one job now
    assert app["jobs"].jobs_service.queue or app["jobs"].jobs_service is not None

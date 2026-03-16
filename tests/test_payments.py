from backend import create_app


def test_payments_pre_authorize_runs_on_auth():
    app = create_app()
    _ = app["auth"].login("alice", "password123")
    # Charges should have at least one entry after auth
    charges = app["payments"].payments_service.payments_repo._charges
    assert len(charges) >= 1


def test_refund_marks_refunded():
    app = create_app()
    charge_id = app["payments"].charge("alice", 10.0)
    refund_id = app["payments"].refund(charge_id)
    assert refund_id.startswith("refund-")

from backend.shared.utils.circular_a import ping_a


def ping_b():
    return "b->" + ping_a()

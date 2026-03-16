from backend.shared.utils.circular_b import ping_b


def ping_a():
    return "a->" + ping_b()

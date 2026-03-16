"""Deprecated utility functions that are not referenced by the codebase."""

def legacy_sum(a, b):
    return a + b


def legacy_divide(a, b):
    if b == 0:
        return None
    return a / b

# Intentional dead function

def unused_legacy_feature(flag=False):
    return flag

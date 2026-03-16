# Deliberately unused service to test dead code detection
class UnusedService:
    def __init__(self):
        self.state = {}

    def do_nothing(self):
        return None

    def never_called(self):
        return "never-called"

class JobsRepository:
    def __init__(self):
        self.queue = []

    def enqueue_job(self, name: str, payload: dict):
        self.queue.append({"name": name, "payload": payload})
        return len(self.queue)

    def dequeue_job(self, name: str):
        for idx, job in enumerate(self.queue):
            if job["name"] == name:
                return self.queue.pop(idx)
        return None

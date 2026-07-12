class KernelScheduler:

    def __init__(self):

        self._tasks = []

    def register(self, task):

        self._tasks.append(task)

    def tasks(self):

        return tuple(self._tasks)
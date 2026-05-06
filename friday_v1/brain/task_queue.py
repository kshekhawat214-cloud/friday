import time


class TaskQueue:

    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def run(self):

        responses = []

        while self.tasks:

            task = self.tasks.pop(0)

            response = task()

            if response:
                responses.append(response)

            time.sleep(0.5)  # small delay between tasks

        return responses


task_queue = TaskQueue()
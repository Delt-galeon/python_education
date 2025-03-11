# add_task.py
from task import Task


class AddTask:
    def __init__(self, task_name, tasks, index_counter):
        self.task_name = task_name
        self.tasks = tasks
        self.index_counter = index_counter

    def execute(self):
        """새로운 할 일 추가"""
        task = Task(self.index_counter, self.task_name)
        self.tasks.append(task)
        self.index_counter += 1
        print(f"할 일 '{self.task_name}'가 추가되었습니다.")

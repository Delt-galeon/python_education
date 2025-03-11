# add_task.py
from task import Task
import json


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
        self.save_to_json()
        print(f"할 일 '{self.task_name}'가 추가되었습니다.")

    def save_to_json(self):
        """할 일 목록을 JSON 파일에 저장"""
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(
                [task.__dict__ for task in self.tasks], f, ensure_ascii=False, indent=4
            )

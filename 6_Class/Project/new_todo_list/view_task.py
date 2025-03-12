# view_task.py
import json
from task import Task


class ViewTasks:
    def __init__(self, tasks):
        self.tasks = tasks

    def execute(self):
        """할 일 목록 조회"""
        if self.tasks:
            print("\n--- 할 일 목록 ---")
            for task in self.tasks:
                print(task)
        else:
            print("할 일이 없습니다.")

# delete_task.py
import json


class DeleteTask:
    def __init__(self, task_index, tasks):
        self.task_index = task_index
        self.tasks = tasks

    def execute(self):
        """할 일 삭제"""
        for task in self.tasks:
            if task.index == self.task_index:
                self.tasks.remove(task)
                self.save_to_json()
                print(f"할 일 '{self.task_index}'가 삭제되었습니다.")
                return
        print(f"할 일 인덱스 '{self.task_index}'을 찾을 수 없습니다.")

    def save_to_json(self):
        """할 일 목록을 JSON 파일에 저장"""
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(
                [task.__dict__ for task in self.tasks], f, ensure_ascii=False, indent=4
            )

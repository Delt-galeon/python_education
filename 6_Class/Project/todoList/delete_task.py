# delete_task.py
class DeleteTask:
    def __init__(self, task_index, tasks):
        self.task_index = task_index
        self.tasks = tasks

    def execute(self):
        """할 일 삭제"""
        for task in self.tasks:
            if task.index == self.task_index:
                self.tasks.remove(task)
                print(f"할 일 '{self.task_index}'가 삭제되었습니다.")
                return
        print(f"할 일 인덱스 '{self.task_index}'을 찾을 수 없습니다.")

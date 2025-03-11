# update_task.py
class UpdateTask:
    def __init__(self, task_index, new_task_name, tasks):
        self.task_index = task_index
        self.new_task_name = new_task_name
        self.tasks = tasks

    def execute(self):
        """할 일 이름 수정"""
        for task in self.tasks:
            if task.index == self.task_index:
                task.name = self.new_task_name
                print(f"할 일 '{self.task_index}'이 '{self.new_task_name}'로 수정되었습니다.")
                return
        print(f"할 일 인덱스 '{self.task_index}'을 찾을 수 없습니다.")

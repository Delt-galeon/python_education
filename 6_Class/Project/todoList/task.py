# task.py

class Task:
    def __init__(self, index, name, status="미완료"):
        """할 일 초기화"""
        self.index = index  # 고유 인덱스
        self.name = name
        self.status = status

    def mark_completed(self):
        """할 일을 완료로 표시"""
        self.status = "완료"

    def mark_pending(self):
        """할 일을 미완료로 표시"""
        self.status = "미완료"

    def __str__(self):
        """할 일의 문자열 표현"""
        return f"[{self.index}] {self.name} ({self.status})"

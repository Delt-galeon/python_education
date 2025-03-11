# member.py
import json
import os


class MemberManager:
    FILE_PATH = "members.json"

    def __init__(self):
        """회원 정보를 관리하는 클래스 초기화"""
        if not os.path.exists(self.FILE_PATH):
            # 파일이 없으면 빈 목록을 저장
            with open(self.FILE_PATH, "w") as f:
                json.dump([], f)

    def _load_members(self):
        """파일에서 회원 정보를 불러옵니다."""
        try:
            with open(self.FILE_PATH, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # JSONDecodeError가 발생하면 빈 리스트를 반환
            return []

    def _save_members(self, members):
        """회원 정보를 파일에 저장합니다."""
        with open(self.FILE_PATH, "w") as f:
            json.dump(members, f, ensure_ascii=False, indent=4)

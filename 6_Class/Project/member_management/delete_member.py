# delete_member.py
from member import MemberManager


class DeleteMember:
    def __init__(self, email):
        self.email = email

    def execute(self):
        """회원 삭제 처리"""
        manager = MemberManager()
        members = manager._load_members()
        updated_members = [
            member for member in members if member["email"] != self.email
        ]
        if len(members) != len(updated_members):
            manager._save_members(updated_members)
            print(f"{self.email}님의 정보가 삭제되었습니다.")
        else:
            print(f"{self.email}님을 찾을 수 없습니다.")

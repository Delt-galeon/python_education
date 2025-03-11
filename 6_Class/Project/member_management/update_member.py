# update_member.py
from member import MemberManager


class UpdateMember:
    def __init__(self, old_email, updated_info):
        self.old_email = old_email
        self.updated_info = updated_info

    def execute(self):
        """회원 정보 수정 처리"""
        manager = MemberManager()
        members = manager._load_members()
        for member in members:
            if member["email"] == self.old_email:
                member.update(self.updated_info)
                manager._save_members(members)
                print(f"{self.old_email}님의 정보가 수정되었습니다.")
                return
        print(f"{self.old_email}님을 찾을 수 없습니다.")

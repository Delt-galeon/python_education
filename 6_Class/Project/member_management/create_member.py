# create_member.py
from member import MemberManager


class CreateMember:
    def __init__(self, member_info):
        self.member_info = member_info

    def execute(self):
        """회원 가입 처리"""
        manager = MemberManager()
        members = manager._load_members()
        members.append(self.member_info)
        manager._save_members(members)
        print(f"{self.member_info['name']}님의 회원가입이 완료되었습니다.")

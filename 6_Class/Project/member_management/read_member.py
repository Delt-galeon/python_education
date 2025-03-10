# read_member.py
from member import MemberManager


class ReadMember:
    def execute(self):
        """회원 목록 조회 처리"""
        manager = MemberManager()
        members = manager._load_members()
        if members:
            print("\n--- 회원 목록 ---")
            count = 0
            for member in members:
                count += 1
                print(
                    f"ID:{count} ,이름: ({member['name']}), 이메일: ({member['email']}), 전화번호: {member['phone']}"
                )
        else:
            print("등록된 회원이 없습니다.")

# main.py
from create_member import CreateMember
from update_member import UpdateMember
from delete_member import DeleteMember
from read_member import ReadMember

def main_program():
    while True:
        print("\n*** 회원 관리 프로그램 ***")
        print("1. 회원 가입")
        print("2. 회원 정보 수정")
        print("3. 회원 삭제")
        print("4. 회원 목록 조회")
        print("5. 종료")

        choice = input("원하는 작업을 선택하세요 (1, 2, 3, 4, 5): ")

        if choice == '1':
            name = input("이름을 입력하세요: ")
            email = input("이메일을 입력하세요: ")
            phone = input("전화번호를 입력하세요: ")
            member_info = {'name': name, 'email': email, 'phone': phone}
            create_member = CreateMember(member_info)
            create_member.execute()

        elif choice == '2':
            old_email = input("수정할 회원의 이메일을 입력하세요: ")
            updated_info = {}
            new_name = input("새로운 이름을 입력하세요 (변경 없으면 Enter): ")
            if new_name:
                updated_info['name'] = new_name
            new_phone = input("새로운 전화번호를 입력하세요 (변경 없으면 Enter): ")
            if new_phone:
                updated_info['phone'] = new_phone
            update_member = UpdateMember(old_email, updated_info)
            update_member.execute()

        elif choice == '3':
            email = input("삭제할 회원의 이메일을 입력하세요: ")
            delete_member = DeleteMember(email)
            delete_member.execute()

        elif choice == '4':
            read_member = ReadMember()
            read_member.execute()

        elif choice == '5':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

# 프로그램 실행

if __name__ == "__main__" : 
    main_program()

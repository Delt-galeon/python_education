# main.py
from add_task import AddTask
from update_task import UpdateTask
from delete_task import DeleteTask
from view_task import ViewTasks


def main_program():
    tasks = []  # 할 일 목록
    index_counter = 1  # 인덱스 번호 시작

    # 기본 데이터로 몇 개의 할 일을 추가
    add_task_1 = AddTask("Python 공부", tasks, index_counter)
    add_task_1.execute()
    index_counter += 1

    add_task_2 = AddTask("프로젝트 코드 리뷰", tasks, index_counter)
    add_task_2.execute()
    index_counter += 1

    add_task_3 = AddTask("운동하기", tasks, index_counter)
    add_task_3.execute()
    index_counter += 1

    while True:
        print("\n*** TODO 리스트 관리 프로그램 ***")
        print("1. 할 일 추가")
        print("2. 할 일 수정")
        print("3. 할 일 삭제")
        print("4. 할 일 목록 조회")
        print("5. 할 일 완료로 표시")
        print("6. 할 일 미완료로 표시")
        print("7. 종료")

        choice = input("원하는 작업을 선택하세요 (1, 2, 3, 4, 5, 6, 7): ")

        if choice == "1":
            task_name = input("추가할 할 일의 이름을 입력하세요: ")
            add_task = AddTask(task_name, tasks, index_counter)
            add_task.execute()
            index_counter += 1

        elif choice == "2":
            task_index = int(input("수정할 할 일의 인덱스를 입력하세요: "))
            new_task_name = input("새로운 할 일의 이름을 입력하세요: ")
            update_task = UpdateTask(task_index, new_task_name, tasks)
            update_task.execute()

        elif choice == "3":
            task_index = int(input("삭제할 할 일의 인덱스를 입력하세요: "))
            delete_task = DeleteTask(task_index, tasks)
            delete_task.execute()

        elif choice == "4":
            view_tasks = ViewTasks(tasks)
            view_tasks.execute()

        elif choice == "5":
            task_index = int(input("완료로 표시할 할 일의 인덱스를 입력하세요: "))
            for task in tasks:
                if task.index == task_index:
                    task.mark_completed()
                    print(f"할 일 '{task_index}'가 완료되었습니다.")
                    break

        elif choice == "6":
            task_index = int(input("미완료로 표시할 할 일의 인덱스를 입력하세요: "))
            for task in tasks:
                if task.index == task_index:
                    task.mark_pending()
                    print(f"할 일 '{task_index}'가 미완료로 변경되었습니다.")
                    break

        elif choice == "7":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    # 프로그램 실행
    main_program()

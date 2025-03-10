
```
todo_list/
│── main.py           # 메인 실행 파일
│── task.py           # Task 클래스를 정의
│── add_task.py       # 할 일 추가 기능
│── update_task.py    # 할 일 수정 기능
│── delete_task.py    # 할 일 삭제 기능
│── view_task.py      # 할 일 목록 조회 기능
│── tasks.json        # 할 일 데이터 저장 파일
```


> TaskManager 클래스는 더 이상 존재하지 않으며, 모든 CRUD 작업은 각 클래스에서 독립적으로 처리됩니다.

> AddTask: 할 일 추가 기능을 담당하는 클래스입니다. execute() 메서드를 통해 할 일을 추가합니다.

> UpdateTask: 할 일 수정 기능을 담당하는 클래스입니다. execute() 메서드를 통해 인덱스를 기준으로 할 일을 수정합니다.

> DeleteTask: 할 일 삭제 기능을 담당하는 클래스입니다. execute() 메서드를 통해 인덱스를 기준으로 할 일을 삭제합니다.

> ViewTasks: 할 일 목록을 조회하는 기능을 담당하는 클래스입니다. execute() 메서드를 통해 할 일 목록을 출력합니다.

> main.py: 사용자가 입력한 값을 기반으로 각 클래스의 메서드를 호출하여 할 일 목록을 관리합니다. 각 CRUD 기능은 각 클래스의 메서드 내에서 실행됩니다.
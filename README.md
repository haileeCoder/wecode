# 오늘 시험에서 사용했던 git 명령어 3개 정리

1. git --version
    - 내 컴퓨터에 git이 설치되어 있는지 확인
    - 이후 git init 명령어를 통해 폴더 내에 숨겨진 git 디렉토리 생성할 수 있다.

2. git status
    - git 트랙한 현재 상황 조회 가능

3. git add .
    - 폴더 내 모든 파일을 커밋하겠다는 뜻!
    - 파일 명을 명시해주면 특정 파일만  커밋할 수 있다. 

4. git commit
    - staging area에 올라있는 파일을 내가 지정한 레포지토리에 commit 하겠다는 뜻!

5. git push origin master
    - git remote add origin 원격저장소URL   -> 통해서 github  원격 저장소와 연결
    - origin 이라는 원격 저장소 내 master 브랜치에 push 하는 것!
    
6. git log
    - 작업 이력 확인
    
7. branch 확인
    - git branch @@@            -> @@@라는branch 생성하겠다는 뜻!
    - git checkout mybranch     -> 생성된 새로운 branch로 전환! 

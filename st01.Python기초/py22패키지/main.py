
# 패키지는 모듈을 계층적, 폴더 단위로 관리하는 방법
# 네임스페이스 라고도 한다.

# 패키지의 모듈을 사용해보겠습니다. 다음 내용을 프로젝트 폴더(C:\project) 안에 main.py 파일로 저장한 뒤 실행해보세요(main.py 파일을 game.graphic 패키지 폴더 안에 넣으면 안 됩니다).
#
# import 패키지.모듈
# 패키지.모듈.변수
# 패키지.모듈.함수()
# 패키지.모듈.클래스()
# main.py

##################
# __init__.py 파일을 꼭 만들자! (없어도 문제는 없지만 레벨이 낮은 프로그램에서 가동시 오류발생)
##################
# ../ ==> 부모 폴더의. open terminal 뒤에 cd ../ 입력하면 윗단계 폴더로 이동
# .. ==> 부모의

# game.graphic 패키지의 geometry 모듈을 가져옴
# game.sound 패키지의 echo 모듈을 가져옴
# game.operation 패키지의 run 모듈을 가져옴

# game.graphic 패키지 geometry 모듈의 triangle_area 함수 사용

# game.graphic 패키지 geometry 모듈의 rectangle_area 함수 사용

# game.graphic 패키지 test 모듈의 test_graphic 함수 사용

# game.operation 패키지 run 모듈의 render_test 함수 사용
### id() > 메모리 주소 확인하는 함수

# 문자열은 수정할 수 없다
# 새롭게 메모리가 할당된다는 의미다.

str1 = "abc"
print("str1 주소값 출력", id(str1) )
print()

str2 = str1 # 주소값 복사 발생
print("str1 주소값 출력", id(str1) )
print("str2 주소값 출력", id(str2) ) # 두 개의 값이 같을 것이다.
print()

str1 = "efg" # 신규 메모리가 할당된다
print("str1 주소값 출력", id(str1) )
print("str2 주소값 출력", id(str2) )
print()

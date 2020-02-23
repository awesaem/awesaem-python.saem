
# 숫자가 아닌 것을 정수로 변환하려고 할 때
try :
     i=int("안녕하세요") 
     print(i) #문장이 실행되지 않음
except ValueError :
    pass #넘어간다 #문제 점프


# 숫자가 아닌 것을 실수로 변환 할 때
try:
    f=float("안녕하세요") 
    print(f)
except ValueError :
    pass


# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환 할 때
try:
    i=int("52.273")
except ValueError :
    pass


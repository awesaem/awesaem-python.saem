# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"

#################################
# 문자열 연산자
#################################

# 문자열 결합 연산자 : +
# "A barking Dog never Bites!"를 출력하시오.
bite = " never Bites!"
str = prov + bite
print ( str ) # "A barking Dog never Bites!"

# 문자열 반복 연산자 : *

# 문자열 일치 연산자 : ==


# 문자열 슬라이싱 연산자 : [ ]
# 문자열 자체가 리스트 취급을 당하기 때문에 그냥 리스트에서 특정 구문을 빼오듯이 쓰면 된다.
# (2번째부터 4번째 자리까지 추출:  bar)
bar = prov[2:5] # bar # 5= 2 + 0 + 1 + 2
print ( bar )

# 문제. Dog 를 추출하여 출력하시오
# index, find 사용
idx = prov.find ("Dog")
if idx == -1 :
    pass
else:
    dog = prov [ idx : idx + 3 ]
    print( dog )
    
    # if idx != -1 : print(dog)c

# 문자열 추출:
# "A barking dog"에서 마지막 g 빼고 "A barking do" 를 출력하시오.


# 첫번째 b 문자를 찾고 출력하시오.

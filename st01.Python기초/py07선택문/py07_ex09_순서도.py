A = input("값을 입력하세요 : ")
B = input("값을 입력하세요 : ")

# 문자열에는 *, + 연산자가 있다
# 문자열에는 / 연산자가 없다.
A = int(A)
B = int(B)
AVG = (A+B)/2


if AVG >= 160 :
    print("합격")
else:
    print("불합격")
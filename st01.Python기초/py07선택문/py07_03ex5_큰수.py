x = input("첫번째 정수 : ")
y = input("두번째 정수 : ")

#문자열로 비교할 때와 숫자열로 비교할 때의 값이 다르므로 주의해야 함
x = int(x)
y = int(y)

if x > y : 
    print(x)
else:
    print(y)
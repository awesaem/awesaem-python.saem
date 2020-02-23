a = input("첫번째 수를 입력하세요 : ")
b = input("두번째 수를 입력하세요 : ")
c = input("세번째 수를 입력하세요 : ")

a = int(a)
b = int(b)
c = int(c)

if a >= b :
    if  a >= c :
        print("입력 받은 수중 가장 큰 수는 %d입니다." % (a))
    else:
        print("입력 받은 수중 가장 큰 수는 %d입니다." % (c))
else:
    if b >= c :
        print("입력 받은 수중 가장 큰 수는 %d입니다." % (b))
    else:
        print("입력 받은 수중 가장 큰 수는 %d입니다." % (c))

# elif 사용시

a = input("첫번째 수를 입력하세요 : ")
b = input("두번째 수를 입력하세요 : ")
c = input("세번째 수를 입력하세요 : ")

a = int(a)
b = int(b)
c = int(c)

if a >= b and a >= c :
    print("입력 받은 수중 가장 큰 수는 %d입니다." % (a))
elif b >= c :
    print("입력 받은 수중 가장 큰 수는 %d입니다." % (b))
else :
    print("입력 받은 수중 가장 큰 수는 %d입니다." % (c))

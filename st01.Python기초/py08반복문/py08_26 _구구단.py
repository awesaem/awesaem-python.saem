
i = input ( " 시작값을 입력하세요. ")
j = input ( " 종료값을 입력하세요. ")

i = int(i)
j = int(j)

if i>j:
    temp = i
    i = j
    j = temp

for x in range(i, j+1, 1) :
    for y in range(1, 10, 1) :
        str= "%2s*%s=%3s" % ( x, y, x * y ) # %2s, %3s는 자릿수 맞추기 위해서
        if y==9:
            print ( str , end="." )
        else:
            print ( str , end=", " )

        # 줄바꿈
    print ( )
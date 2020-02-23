# 무한루프 만들기
    # 시작단 입력받기
    # 루프탈출. 시작단이 양수가 아니면 또는 종료단이 양수가 아니면
        # 무한 루프 탈출
    # swap. 시작단이 종료단보다 크다면
        # 시작단과 종료단 값 교환. swap
    # 구구단 출력


i = input ( " 시작값을 입력하세요. ")
j = input ( " 종료값을 입력하세요. ")

i = int(i)
j = int(j)

while i <= 0 or j <= 0 : 
    i = input ( " 시작값을 입력하세요. ")
    j = input ( " 종료값을 입력하세요. ")
    i = int(i)
    j = int(j)
    if (i > 0 and j > 0) :
        continue
        
if i > j :
    temp = i
    i = j
    j = temp

for a in range(i, j+1, 1) :
    for b in range(1, 10, 1) :
        str= "%2s*%s=%3s" % ( a, b, a * b ) # %2s, %3s는 자릿수 맞추기 위해서
        if b==9:
            print ( str , end="." )
        else:
            print ( str , end=", " )

        # 줄바꿈
    print ( )
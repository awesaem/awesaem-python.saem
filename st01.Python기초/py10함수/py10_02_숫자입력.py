# 1부터 10까지의 합계를 구하고
# 그 합계를 sum에 저장하고 sum 값을 한번만 출력한다.

sum = 0
for i in range(1, 11, 1):
    sum = sum + i
str = "%s부터 %s까지의 합계 : " % (1, 10)
print ( str , sum)

# 1부터 100까지의 합계를 구하고
# 그 합계를 sum2에 저장하고 sum2 값을 한번만 출력한다.
sum2 = 0
for i in range(1, 101, 1):
    sum2 = sum2 + i
str = "%s부터 %s까지의 합계 : " % (1, 100)
print ( str , sum2)

# 100부터 sum2까지의 합계를 구하고
# 그 합계를 sum3에 저장하고 sum3 값을 한번만 출력한다.
sum3 = 0
for i in range(100, sum2+1, 1):
    sum3 = sum3 + i
str = "%s부터 %s까지의 합계 : " % (100, sum2)
print ( str , sum3)


# 반복되는 코드는 함수를 만들어 사용한다.
# get_sum() 함수를 만듦 
# 바뀌는 값을 입력으로 처리한다. 입력이란 매개변수다.
# 매개 변수는 함수에서 입력으로 사용되는 변수

def get_sum( a , b ): # a 부터 b 까지 합계를 구하시오
    sum4 = 0
    for i in range( a , b+1 , 1):
        sum4 = sum4 + i
    str = "%s부터 %s까지의 합계 : " % ( a , b )
    print ("함수출력" , str , sum4)

    return sum4

#return 변수명



# 함수 호출 = 함수 사용
#get_sum( 1 , 10 ) # 1부터 10까지의 합계를 구하고 출력
#get_sum( 1 , 100 ) # 1부터 100까지의 합계를 구하고 출력
#get_sum( 100 , sum2 ) # 100부터 10까지의 합계를 구하고 출력

sum1 = get_sum(1,10)
sum2 = get_sum(1,100)
sum3 = get_sum(100, sum2)


# a = 시작 숫자
# b = 마지막 숫자
# a 부터 b 까지 총 갯수 = b - a + 1
# a 부터 b 까지 숫자의 합 = { ( b - a + 1) * ( a + b ) } / 2 = - a**2 + a + b**2 + b
                                  # = b**2 - a**2 + a + b 

def got_sum ( a , b ) :
    result = (b**2 - a**2 + a + b ) / 2
    return result

sum1 = got_sum( 1 , 10 )
sum2 = got_sum( 1 ,100 ) 
sum3 = got_sum( 100 , sum2 )

print (sum1)
print (sum2)
print (sum3)
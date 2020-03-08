
import math # 파이(PI) = 3.14.... 변수를 사용하기 위해서 import
# r = radius

def calCircle( r ) :
    #반지름이 r인 원의 넓이와 둘레를 동시에 반환하는 함수 ( area, circum )
    area = math.pi * r * r # math.pi * r**2
    circum = 2 * math.pi * r
    return ( area, circum )


def main() :
    str = input("원의 반지름을 입력하시오 : ")
    radius = float( str ) # 실수로 변환
    ( a , c ) = calCircle( radius )
    
    tmp = "원의 넓이는 %10.4f , 둘레는 %10.4f 이다" % ( a, c )
    print ( tmp )
    
    
# main 함수 호출

if __name__ == "__main__":
    main() ####파이썬의 메인 함수 불러오는 규칙
# 피보나치 수열 모듈

def fib (n) : # 피보나치 수열을 화면에 출력한다.
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()
    
def fib2(n) : # 피보나치 수열을 리스트로 변환
    result = [ ]
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    retun result
    
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    
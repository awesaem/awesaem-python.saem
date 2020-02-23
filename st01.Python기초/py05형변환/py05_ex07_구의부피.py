# 반지름이 5인 구의 부피를 계산하는 파이썬 프로그램을 작성해보자. 

r = input("구의 반지름을 입력하시오 >> ")

import math
pi = float(math.pi)

volume = (4 / 3) * pi * (float(r)**3)

print(volume)
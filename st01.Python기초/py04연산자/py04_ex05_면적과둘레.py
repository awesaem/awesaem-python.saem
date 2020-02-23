
w=input("가로:")
h=input("세로:")

area=int(w)*int(h)
perimeter=2*(int(w)+int(h))

print("넓이:",area)
print("둘레:",perimeter)



#정답
w = input("너비 값을 입력하시오 >> ") #문자열
h = input("높이 값을 입력하시오 >> ") #문자열

w=float(w) #실수로 형변환
h=float(h) #실수로 형변환

area = w*h
perimeter = 2 * (w+h)

print("사각형의 넓이 : ",area)
print("사각형의 둘레 : ",perimeter)
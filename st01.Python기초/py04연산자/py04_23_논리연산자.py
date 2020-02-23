x=3
y=4

r=((x==3) and (y==3)) #False
print("(x==3) and (y==3) : ",r)

r=((x==3) and (y!=3)) #True
print("(x==3) and (y!=3) : ", r)

r=((x==3) or (y==3)) #True
print("(x==3) or (y==3) : ", r)

r= ((x==3) or (y==4)) #True
print("(x==3) or (y==4) : ", r)

r=((x!=3) or (y==4)) #True
print("(x!=3) or (y==4) : ", r)

r=((x!=3) or (y!=4)) #False
print("(x!=3) or (y!=4) : ", r)


#변수 선언과 초기화
x=3
y=4
print((x==y) and (x!=y)) #False
print((x>y) or (x<y)) #True
print((x>=y) or (x<=y)) #True
print((x==y) and (x!=y) or (x<y)) #False > True... why?

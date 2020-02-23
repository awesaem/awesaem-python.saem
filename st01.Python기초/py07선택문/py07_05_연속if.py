# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고    
# 90점 이상이면 A,    
# 80점 이상이면 B,    
# 70점 이상이면 C,   
# 60점 이상이면 D,    
# 나머지는 F

grade = input("Grade : ")
grade = int(grade)

if 90 <= grade <= 100 :
    print ("학점 : A")
elif 80 <= grade < 90 :
    print ("학점 : B")
elif 70 <= grade < 80 :
    print ("학점 : C")
elif 60 <= grade < 70 :
    print ("학점 : D")
else :
    print ("학점 : F")
    

#비교 연산자만 사용한 방법
#순서만 잘 맞추면 가능

grade = input("Grade : ")
grade = int(grade)

if 90 <= grade :
    print ("학점 : A")
elif 80 <= grade :
    print ("학점 : B")
elif 70 <= grade :
    print ("학점 : C")
elif 60 <= grade :
    print ("학점 : D")
else :
    print ("학점 : F")
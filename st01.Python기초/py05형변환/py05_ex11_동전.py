# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자. 
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다. 
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 
# 거스름돈을 계산하여서 동전으로 반환한다. 

price = input("물건값을 입력하시오: ")
thousand = input("1000원 지폐개수: ")
fiveHundred = input("500원 동전개수: ")
oneHundred = input("100원 동전개수: ")

change = (int(thousand)*1000) + (int(fiveHundred)*500) + (int(oneHundred)*100) - int(price)

# 거스름돈(500원 동전 개수)을 계산한다. 
changeFiveHundred = change//500
print(changeFiveHundred,"원")

# 거스름돈(100원 동전 개수)을 계산한다. 
change=change-changeFiveHundred*500
changeHundred = change%500//100
print(changeHundred,"원")

# 거스름돈(10원 동전 개수)을 계산한다. 
change=change-changeHundred*100
changeTen = change%100//10
print(changeTen,"원")

# 거스름돈(1원 동전 개수)을 계산한다. 
change=change-changeTen*10
changeOne = change%10
print(changeOne,"원")

# 출력

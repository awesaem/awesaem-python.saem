# 24달러를 정기예금으로 382년 묶어놓은 결과는? 복리는 6%

init_money = 24
interest = 0.06
years = 382

final_money = float(init_money) * (float(interest)+1)**int(years)
print(final_money)

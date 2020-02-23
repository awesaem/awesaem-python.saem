init_potato = 20
week_potato = 10
gain_potato = 40
daily_potato = 3

year_days = 365
week = int(year_days) // 7

#1년치 수확량 = 기존감자 + 매주 수확량 - ( 매주 심은 양 + 매주 먹은 양 )
final_potato = int(init_potato) + int(week)*int(gain_potato) - (int(week_potato)*int(week)) - (int(daily_potato) * int(year_days))

print(final_potato)
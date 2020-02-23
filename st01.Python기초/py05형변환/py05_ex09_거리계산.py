# 지구에서 가장 가까운 별은 프록시마 켄타우리 (Proxima Centauri)
# 지구와 프록시마 켄타우리 간의 거리 = 40 * 10^12
# 빛의 속도로 프록시마 켄타우리까지 가는 데 걸리는 시간은?

speed = 3*(10**5)
distance = 4*(10**13)
secs = float(distance)/float(speed)
print(secs, "초")

#연수로 환산
light_year = secs / (60.0*60.0*24.0*365.0)
print(light_year, "년") 

#소수점 0자리수
light_year = secs // (60.0*60.0*24.0*365.0)
print(int(light_year), "년") 

#소수점 2자리수
light_year = secs / (60.0*60.0*24.0*365.0)
print("%0.2f년" % (light_year)) 
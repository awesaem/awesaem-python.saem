# 서브에서 생긴 에러를 메인으로 던진다
# 예외를 강제로 발생시킨다

# An exception flew by!
# Traceback(most recent call last):
#     File "<stdin>", line 2, in < module >
# NameError: HiThere

try:
    raise NameError("HiThere") # 예외를 던진다
except NameError :
    pass
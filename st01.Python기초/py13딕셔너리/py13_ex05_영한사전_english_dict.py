english_dict = dict()

# C: 딕셔너리 추가
# dictionary["key"] = "value"

english_dict["one"] = "하나"
english_dict["two"] = "둘"
english_dict["three"] = "셋"


# .get() 메서드 사용
# .get() 메서드 키가 존재하지 않는 경우에 None을 반환한다.
word = input( "단어를 입력하시오: " )
print ( english_dict.get(word, "없음"))



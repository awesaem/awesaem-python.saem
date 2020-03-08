# 딕셔너리의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle

# 딕셔너리 선언하기
dictionary = {
    "name" : "망고",
    "type" : "당",
    "ingredient" : ["망고", "설탕", "소금", "치자" ],
    "orgin" : "필리핀"
}
# 요소 추가 전에 내용을 출력해봅니다.
print( dictionary ) #전체출력
print( dictionary["name"] ) #개별출력
print( dictionary["type"] )
print( dictionary["ingredient"] )
print( dictionary["orgin"] )

# C: 딕셔너리 추가
dictionary["head"] = "머리"
dictionary["body"] = "몸"

# 선택 연산자 [ ] 로 딕셔너리 읽기
# dictionary의 head 값을 출력하시오
print( "head 값", dictionary["head"] )
print( "head 값", dictionary.get("head") )

# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
# try ~ except 를 추가하시오.
try:
    dictionary["존재하지 않는 키"] # KeyError
except KeyError as ex:
    print ( ex ) # 화면에 에러 출력하고 다른 라인 실행
 


# U : 딕셔너리 수정
# name 값을 "8D 망고" 로 수정하시오
print ( "name", dictionary["name"])
dictionary["name"] = "8D 망고" # "7D 망고" --> "8D 망고"  변경
print ( "name", dictionary["name"])


# D: 딕셔너리 삭제.
# 1. 연산자 방식 ==> del. 비추천
# 2. 메서드 방식 ==> .pop("key"). 추천
# name, type 키를 삭제
print( "삭제 전", dictionary)
dictionary.pop("name")
dictionary.pop("type")
print( "삭제 후", dictionary)


# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생. ==> try ~ except 를 추가
# 딕셔너리 키 존재 여부 확인 
# 방법1 .get() 메서드 사용
# .get() 메서드 키가 존재하지 않는 경우에 None을 반환한다.
value = dictionary.get("존재하지 않는 키") # value 값이 None 이면 키가 없다는 의미다.
if value == None :
    print("키가 존재하지 않는다.")
else:
    print("키가 존재한다.")
    print( value )
# 방법2 in 연산자 사용
if "존재하지 않는 키" in dictionary : 
    print("키가 존재한다.")
    print(dictionary["존재하지 않는 키"])
else:
    print("키가 존재하지 않는다.")


# S: 정렬. 딕셔너리는 정렬하는 방법이 없다.
# 단, key 값만 정렬 가능, value 값만 정렬은 가능 (전체 정렬이 불가능하다는 것)

# S: 검색. 특별한 방법이 없다. 
# 선택연산자를 사용하면 바로 검색되기 때문



########################
# 딕셔너리 열거
########################

# key 만 열거. .keys() 매서드 사용
for key in dictionary.keys():
    print( "keys >>>", key )

# value 만 열거. .values() 매서드 사용
for value in dictionary.values():
    print( "values >>>", value )
    
# key, value를 쌍으로 열거. .items() 매서드 사용
for item in dictionary.items():
    print( "items >>>", item )
    
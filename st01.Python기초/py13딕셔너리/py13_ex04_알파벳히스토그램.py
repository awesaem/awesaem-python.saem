# 작업순서
# 1. 파일 읽고 문자열에 텍스트 저장
#### 줄바꿈 (\n) 을 제거한다. str = str.replace("\n", " ")
# 2. 딕셔너리 table 을 만든다.
# 3. 문자열을 split( ) 해서 array 리스트로 만든다.
# 4. 반복문을 사용하여 array 리스트를 루프 돌면서
# 4-1. 리스트 요소에서 첫글자를 추출한다. 선택연산자 [ ] 사용
#       val = array[i][0] 또는 val = i[0]
#### 대소문자 구분을 하지 않기 위해 소문자로 치환한다 ==> val = val.lower()
# 4-2. 딕셔너리 table에서 키값중에 val이 있는지 찾는다 ==> table에서 찾을 때는 get( ) 메서드나 in 연산자를 사용한다.
#       찾았다면, table[val]=table[val] + "-"
#       아니면, table[val]="-"
# 5. 찾기가 끝나면 table을 출력한다.


str = """All's well that ends well.
Bad news travels fast.
Well begun is half done.
Birds of a feather flock together."""
str = str.replace("\n", "")
table = { }
array = str.split(" ")

for i in range(0, len(array), 1):
    # print(i) # This, was, a, .....
    # array[0] == This ==> 0번방의 첫글자 추출 array[0][0] == T
    # array[1] == was  ==> 1번방의 첫글자 추출 array[1][0] == w
    # array[2] == a     ==> 2번방의 첫글자 추출 array[2][0] == a
    key = array[ i ][ 0 ] #첫번째 글자 추출
    key = key.upper( )
    tmp = table.get( key ) # table에서 키값으로 찾기

if tmp == None :
   table[ key ] = 1 
else :
   table[ key ] = table[ key ] + 1

# 출력하기. 딕셔너리 키와 값의 쌍으로 열거. items()
for item in table.items():
    print( "items >>>", item[0], item[1] )
    #print( item[0], item[0]*item[1]) item 0을 item[1]번 반복하시오
                                            #item = (A, 17) ==> AAAAAAAAAAAAAAAA
                                            
# 왜 안되냐 답답해 죽겠네
# git hub 에서 이부분 어떻게 했는지 확인하기
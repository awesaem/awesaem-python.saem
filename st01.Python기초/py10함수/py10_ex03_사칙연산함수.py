def Add( first , second ) :
    result = first + second
    return result # 결과 반환

def Minus( first , second ) : 
    result = first - second
    return result

def Mul( first , second ) : 
    result = first * second
    return result

def Div( first , second ) :
    result = 0
     
    try:
        result = first / second
    except ZeroDivisionError as ex:
        print (ex)
    return result


# 입력 받기

x = input ( "First Num : ")
y = input ( "Second Num : ")

x = int(x)
y = int(y)

valueAdd = Add( x , y )
print (valueAdd)
valueMinus = Minus( x , y )
print (valueMinus)
valueMul = Mul( x , y )
print (valueMul)
valueDiv = Div( x , y )
print (valueDiv)
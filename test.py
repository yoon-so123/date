# let a = 3; const b = 'hi';

# a=3
# b = 'hi'
# c = True
# d = False

# print("hello, python!"+b) #js : 문자 + 숫자 = 문자
# #python 은 문자+숫자는 에러 뜹니다.
# print('bye') #console.log("hi");
# print('bye'+ str(a))

# item_name 변수를 만들고 widget 이라는 값 저장
# price 변수를 만들고 23.5 저장 (숫자)
# stock 변수를 만들고 100 저장(숫자)
# is_empty 변수를 만들고 거짓 저장(불)
# item_name 값 띄우고 가격 띄우고 stock 출력
# 예: widget 23.5 100 출력되면됨.

# item_name = 'widget'
# price = 23.5
# stock = 100
# is_empty = False

# print(item_name, price, stock)


# 주민등록번호 = '990101-1111111'
# #문제 - 생년월일만 출력
# #대쉬를 기준으로 왼,오 나눠보겠다.
# print(주민등록번호.split('-'))
# #['990101','1111111'] 이렇게 나옴.

# print(주민등록번호.split('-')[0]) #990101
# print(주민등록번호.split('-')[1]) #1111111

# msg = "안녕하세요 소정님"
# print(msg.split()[1][:2]) # 소정

a= 5
b=1

# b 에다가 a 값 넣고 a 에다 b 값 넣어서 스왑하고 싶다면

'''
let a = 5
let b = 3
let temp
temp = a
a = b
b = temp
'''

a,b = b,a #다중할당 파이썬스러운 코드(Pythonic) 파이썬만 됨.

myList = [1,2,3]

a,b,c = myList
print(a,b,c)

# class 랑 lambda 알면 좋다.
# 데이터분석시 자주 쓰이지 않는다.
# 필요하면 추가적으로 공부하세요

'''
print
변수
자료형
연산
문자열
문자열 인덱싱 슬라이싱 
split()
input()
list
tuple
set
dictionary
if
while
for
zip
enumerate
다중할당
함수 function
'''
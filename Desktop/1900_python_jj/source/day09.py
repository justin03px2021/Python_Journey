from colors import *
from myutils import *

tuple_a = (1,2)
print(tuple_a.index(2))
# tuple_a.pop() #tuple은 조작 안됨 remove도 마찬가지

cprintTitle("Set Method")
a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = a.intersection(b)
d= a.union(b)
e = a.difference(b)
print(c,d,e)

cprintTitle("Dictionary Method")
dic = {1:'one','subject':['science','korean'], '숫자':1234}
print(dic)
# print(dic[1:3]) #dictionary는 순서가 없음
print(dic['숫자'])
print(list(dic.keys())) # keys()의 결과는 dict_key type
print(dic.values())
print(dic.items())

print('dic[1]', dic[1])
print('dic.get(1)', dic.get(1))

# print('dic[8]', dic[8]) #해당 key가 없으면 오류가 난다
print('dic.get(8)', dic.get(8))
print(dic.get(8), "그런 값 없지롱 이 값으로 대체 가능")

person = {'name':'david', 'age':5}

#person에서 꺼내오면 key만 꺼내옴
for item in person:
    print(item, person.get(item))

for item in person.items():
    print(item[0],item[1])

cprintTitle("String")
a = "abcdefg"
print(a)
print(a[0],a[1],a[2],a[5])
print(a[1:3])
print(a[3:])
print(a[3::2])

cprintTitle("Array copy")
a = list(range(1,11))
print(a)
b = a[1:8]
print(b)
c = a[1:8:2]
print(c)
d=a[1:]
print(d)

e = (1,2,3,4,5)
f = e [2:]
print(f)

g = {1,2,3,4,5}
# h = g[1:3]    #SET은 index 가 없음

h = g

cprintTitle('User Function')
printMessage1()
printMessage2("Happy")
# printMessage2()
printMessage3()
printMessage3('unhappy')
printMessage4('HHH', 3)
printMessage4(888)
printMessage4(i=10)

val =  getRandomDice(1000)
print(val)

v1, v2, v3 = getMultiDice(100)
print(v1, v2, v3)
v = getMultiDice(100)
print(v)    #리턴값은 여러 개인데 하나로 받는 경우 튜플로 받아짐

s = addAll(2,3,4)
print(s)

# test = input("전화번호 입력 : ")
# a, b, c = checkPhoneNumber(test)
# print(a, b, c)


a = 0
for k in 1,2,3,4:
    a = a + k
    print(a)

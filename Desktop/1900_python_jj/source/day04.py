"""
    Day04 - control statement
    Version : 1.0
    Created : 2022.05.20
    Updated : 2022.05.20
    Author : Justin Jung
"""
from colors import *
print(RED + "while" + END)
print('노가다')
print('1번 출력')
print('2번 출력')
print('3번 출력')
print('4번 출력')
print('5번 출력')
print('6번 출력')
print('7번 출력')
print('8번 출력')
print('9번 출력')
print('10번 출력')
print()

print('자동화')
i = 1
while i < 10:
    print('{}번 출력'.format(i))
    i = i + 1

i = 0
while i < 10:
    i = i + 1
    print(i)

i = 0
# while True:
#         print("막을 수 없어{}".format(i))
#         i = i + 1   #i += 1

# while True:
#     num = input("1에서부터 10까지의 숫자 중 하나를 입력해주세요 : ")
#     if num.isdecimal() == True and int(num) >= 1 and int(num) <= 10 :
#         print('입력하시는 숫자는 {}입니다.'.format(num))
#         break
#     else:
#         print('{}는 잘못입력한 값이잖아.'.format(num))

print(GREEN + 'for' +END)
for s in '문자열들':
    print(s, end='-')

print()
for l in ['first','second','third']: #list
    print(l, end=" ")

print()

season4 = ('Spring','Summer','Fall','Winter') #tuple
for t in season4:
    print(t)

print()
season4 = {'Spring','Summer','Fall','Winter'} #set
for t in season4:
    print(t)

print()
for i in range(1,11):   # range, 11은 포함되지 않음에 유의
    print('{}번 출력'.format(i))

print()
person = {'name':"py",'age':[100,200,300]}
for i in person:
        print(i, person[i], person.get(i))

#dict를 key-value pair로 가져오는 방법
for key, item in person.items():
    print(key, item)


"""
    Day03 - str, condition
    Version : 1.0
    Created : 2022.05.19
    Updated : 2022.05.19
    Author : Justin Jung
"""
print("Day3 - str.format")
a = 1
print("a의 값은", a)

print("{}은 또 하나의 {}함수 {}입니다".format('이것','print','사용법'))
print("숫자도 되는지 해보죠 {}".format(10))
print("괄호보다 입력이 더 많을 떄는 {} {}".format('되네','궁금합니다','신기하네요'))
# print("괄호보다 입력이 더 적을 때는 {} {}".format('되나요')) # 괄호가 입력보다 더 많을 때는 오류

print("#" * 40)
print("이름:{name} 주소:{addr} 번호:{no}".format(name='파이썬',addr='역삼동',no=103))

print("#" * 40)
print("Day3 - if statement")
a=1
if a > 0:
    print("a는 양수")
if a == 1:
    print("a는 1임")
if not a != 1:
    print("a는 1이 아닌게 아님")

a = -100
if a > 0:
    print('a는 양수2')
     # print("a는 양수 3")  #파이썬은 들여쓰기(indent)가 매우 중요
   # print("a는 양수4")   #윗 줄보다 들여쓰기 레벨이 높아도 안됨
print("a는 양수5")

# if a < 0: print("a는 양수6")
#     print("a는 양수7")   #if문 줄에 실행문을 넣으면 아래줄을 잘 맞춰도 오류

if a < 0: print("a는 양수8"); print('a는 양수9')

# if a = 2:     #파이썬은 이런 것 허용하지 않는다. =가 아니라 ==
#     print("a는 2임")

import colors
print(colors.RED + "if-elif-else" + colors.END)

from colors import *
print(RED + "if-elif-else" + END)
e = -1
if e > 0:
    print("양수")
elif e == 0:
    print("zero")
else:
    print("음수")



"""
    Day03 - 5 min Challenge
    Version : 1.0
    Created : 2022.05.19
    Updated : 2022.05.19
    Author : Justin Jung
"""
'''
    1. "이름을 입력하세요"를 출력하고 입력을 받는다.
    2. "주민번호 맨 뒷자리를 입력하세요"를 출력하고 입력을 받는다. 
    3. 뒷자리가 1,6이면 "월" ..... 5,0이면 "금"
    4. ***님의 접종일은 *요일입니다. 요일 지켜서 오세요
'''

name = input("이름을 입력하세요 :")

fnum = input("주민번호 맨 뒷자리를 입력하세요 :")


if int(fnum) % 5 ==1:
    day = "월"
elif int(fnum) % 5 ==2:
    day = "화"
elif int(fnum) % 5 == 3:
    day = "수"
elif int(fnum) % 5 ==4:
    day = "목"
else:
    day = "금"

print("{}님의 접종일은 {}요일입니다. 요일 지켜서 오세요".format(name,day))

# if fnum in "16" : day = "월"
# elif fnum in "27" : day = "화"
# elif fnum in "38" : day = "수"
# elif fnum in "49" : day = "목"
# elif fnum in "50" : day = "금"


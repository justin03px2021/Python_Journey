"""
    Mini Project
    Version : 1.0
    Created : 2022.05.24
    Updated : 2022:05.24
    Author : Justin Jung
"""
"""
    1. 보물상자에서 무기를 5종류 중 랜덤으로 하나를 획득한다. 
    2. 길을 가다가 늑대, 산적, 드래곤 중 랜덤으로 하나를 만난다. 
    3. 무기를 가지고 둘 중 하나의 에너지가 0 일 될 때까지 싸운다. 
    사용자는 공격, 회복 중 하나를 선택하며 상대는 공격만 한다. 
    4. 승리 또는 패배에 따라 메시지를 출력한다.    
"""
#1. Opening
#1-1. 보물상자를 발견했다는 메시지를 출력하고 사용자가 아무키와 엔터기를 누르기를 기다린다. (보물상자 노란색으로)
#   print, input을 익히기
# 1-2. 보물상자에서 랜덤으로 1개의 무기를 획득한다.
#     각 무기는 [무기이름, 최소공격력, 최대공격력의]의 데이터를 가진다.
#   random, list 익히기
nam = input('이름을 입력하시오: ')
from colors import *
print(YELLOW + '보물 상자'+ END + '를 발견했다!')
i = input(BLACK + 'press enter any key to continue' + END)
import random
rand = random.randint(0, 4)
wpn = ['','','','','']
from colors import *
wpn[0] = RED + '칼' + END
wpn[1] = CYAN + '활' + END
wpn[2] = BLUE + '마법사의 지팡이' + END
wpn[3] = MAGENTA + '방패' + END
wpn[4] = GREEN + '창'+ END

atck = ['','','','','']
atck[0] = random.randint(5, 10)
atck[1] = random.randint(3, 12)
atck[2] = random.randint(2, 15)
atck[3] = random.randint(6,8)
atck[4] = random.randint(4,11)
if rand == 0:
    l=5
    h=10
elif rand == 1:
    l=3
    h=12
elif rand == 2:
    l=2
    h=15
elif rand == 3:
    l=6
    h=8
elif rand == 4:
    l=4
    h=11

w = wpn[rand]
if  w == wpn[0] or w == wpn[1] or w == wpn[4]:
    a = '을'
elif w == wpn[2] or w == wpn[3]:
    a = '를'
print(YELLOW + '보물 상자'+ END + '에서 {}{} 얻었다!'.format(w,a))
i = input(BLACK + 'press enter any key to continue' + END)
print('무기정보')
print('무기이름: {}'.format(w))
print('최소 공격력: {}'.format(l))
print('최대 공격력: {}'.format(h))
job = ['','','','','']
job[0] = RED + '기사' + END
job[1] = CYAN + '궁수' + END
job[2] = BLUE + '마법사' + END
job[3] = MAGENTA + '방패병' + END
job[4] = GREEN + '창기사'+ END
j = job[rand]
if  j == job[0] or j == job[1] or j == job[2] or j == job[4]:
    b = ''
elif j == job[3]:
    b = '으'
print(GREEN + '{}'.format(nam) + END + '님. {}{}로 전직하신 거를 축하합니다!'.format(j, b))
i = input(BLACK + 'press enter any key to continue' + END)
print(GREEN + '{}'.format(nam) + END +'님 당신은 모험을 떠났습니다.')
i = input(BLACK + 'press enter any key to continue' + END)
mon = ['','','']
mon[0] = RED + '드래곤' + END
mon[1] = WHITE + '늑대' + END
mon[2] = CYAN + '산적' + END
rand1 = random.randint(0,2)
m = mon[rand1]
if  m == mon[1]:
    c = '를'
else:
    c = '을'
print('당신은 길을 가던 도중, {}{} 만났습니다.'.format(m,c))
print()
print(m)
pk=15
p = ' '*int(pk)
print('HP:' + GREEN_BG + p + END + " (15/15)")
monHP = 15
print()
print(GREEN + nam + END)
p1k = 10
p1 = ' '*int(p1k)
print('HP:' + GREEN_BG + p1 + END + " (10/10)")
myHP = 10
print()
d1 = input('전투에 대비하시겠습니까? (y/n) 로 답하시오 ')
while True:
    if d1 == 'y':
        print('전투가 시작되었습니다.')
        break
    elif d1 == 'n':
        print('당신은 전투에서 도망치고 패배하였습니다.')
        break
    d1 = input('전투에 대비하시겠습니까? (y/n) 로 답하시오 ')



# while True:
#     d2 = input('선택지를 고르시오. (공격/회복) ')
#     if d2 == '공격' or d2 == '회복':
#         break
# heal = 5
mons_atck = 3
# if d2 == '회복':
#     if myHP < 10:
#         print(myHP + heal + '/10')
#     else:
#         print('이미 풀피입니다.')
# elif d2 == '공격':
#     print('당신은 {}만큼 {}을 공격했습니다.'.format(atck[rand], m, c))
#     print()
#     print('{} HP: '.format(m) +str(monHP-atck[rand]) + '/15')
#     print()
#     print('{} HP:'.format(nam) +str(myHP) + '/10')
#
# i = input(BLACK + 'press enter any key to continue' + END)
if m == mon[1]:
    c = '가'
else:
    c = '이'

# print('{}{} 3만큼 {}님을 공격했습니다.'.format(m, c,nam))
# print('{} HP: '.format(m) +str(monHP-atck[rand]) + '/15')
# print()
# print('{} HP: '.format(nam) +str(myHP-mons_atck) + '/10')
# print()
if d1 == 'y':
    pk=15
    p = ' '*int(pk)
    print('HP:' + GREEN_BG + p + END + " (15/15)")
    monHP = 15
    print()
    print(GREEN + nam + END)
    p1k = 10
    p1 = ' '*int(p1k)
    print('HP:' + GREEN_BG + p1 + END + " (10/10)")
    myHP = 10
    print()


if d1 == 'y':
    while True:
        d2 = input('선택지를 고르시오. (공격/회복) ')
        if d2 == '공격':
            print('당신은 {}만큼 {}을 공격했습니다.'.format(atck[rand], m, c))
            print()
            r = monHP - atck[rand]
            if r <= 0:
                r = 0
            pk = r
            p = ' ' * int(pk)
            if r < 6:
                print('{} HP: '.format(m) + RED_BG + p + END + ' (' + str(r) + '/15)')
            else:
                print('{} HP: '.format(m) + GREEN_BG + p + END + ' (' + str(r) + '/15)')
            print()
            p1k = myHP
            p1 = ' ' * int(p1k)
            if myHP < 4:
                print(GREEN + '{}'.format(nam) + END + ' HP: ' + RED_BG + p1 + END + ' (' + str(myHP) + '/10)')
            else:
                print(GREEN + '{}'.format(nam) + END + ' HP: ' + GREEN_BG + p1 + END + ' (' + str(myHP) + '/10)')
            print()
            monHP = monHP - atck[rand]
            if monHP < 0:
                monHP = 0
            if monHP == 0:
                break
            i = input(BLACK + 'press enter any key to continue' + END)
            print()
            print('{}{} 3만큼 '.format(m, c)+ GREEN + '{}'.format(nam) + END+' 님을 공격했습니다.')
            print()
            pk = monHP
            p = ' ' * int(pk)
            if monHP < 6:
                print('{} HP: '.format(m) + RED_BG + p + END + ' ('+ str(monHP) + '/15)')
            else:
                print('{} HP: '.format(m) + GREEN_BG + p + END + ' (' + str(monHP) + '/15)')
            print()
            p1k = int(myHP - mons_atck)
            p1 = ' ' * int(p1k)
            if myHP - mons_atck < 4:
                print(GREEN + '{}'.format(nam) + END + ' HP: ' + RED_BG + p1 + END + ' (' + str(myHP - mons_atck) + '/10)')
            else:
                print(GREEN + '{}'.format(nam) + END + ' HP: ' + GREEN_BG + p1 + END + ' (' + str(myHP - mons_atck) + '/10)')
            print()
            myHP = myHP - mons_atck
            if myHP < 0:
                myHP = 0
            if myHP == 0:
                break
        elif d2 == '회복':
            print('당신은 2만큼 회복했습니다.')
            print()
            myHP = myHP + 2
            if myHP >= 10:
                myHP = 10
            pk = monHP
            p = ' ' * int(pk)
            if monHP < 6:
                print('{} HP: '.format(m) + RED_BG + p + END + ' (' + str(monHP) + '/15)')
            else:
                print('{} HP: '.format(m) + GREEN_BG + p + END + ' (' + str(monHP) + '/15)')
            print()
            p1k = myHP
            p1 = ' ' * int(p1k)
            if myHP < 4:
                print(GREEN + '{}'.format(nam) + END + ' HP: ' + RED_BG + p1 + END + ' (' + str(myHP) + '/10)')
            else:
                print(GREEN + '{}'.format(nam) + END + ' HP: ' + GREEN_BG + p1 + END + ' (' + str(myHP) + '/10)')
            print()
            i = input(BLACK + 'press enter any key to continue' + END)
            print()
            print('{}{} 3만큼 {}님을 공격했습니다.'.format(m, c, nam))
            print()
            if monHP < 6:
                print('{} HP: '.format(m) + RED_BG + p + END + ' (' + str(monHP) + '/15)')
            else:
                print('{} HP: '.format(m) + GREEN_BG + p + END + ' (' + str(monHP) + '/15)')
            print()
            r1 = myHP - mons_atck
            p1k = r1
            p1 = ' ' * int(p1k)
            if r1 < 4:
                print(GREEN + '{}'.format(nam) + END + ' HP: ' + RED_BG + p1 + END + ' (' + str(r1) + '/10)')
            else:
                print(GREEN + '{}'.format(nam) + END + ' HP: ' + GREEN_BG + p1 + END + ' (' + str(r1) + '/10)')
            print()
            myHP = myHP - mons_atck
            if myHP < 0:
                myHP = 0
            if myHP == 0:
                break
if monHP == 0:
    print('축하합니다! 당신은 첫 전투에서 승리하셨습니다.')
if myHP == 0:
    print('당신은 첫 전투에서 패배하셨습니다.')


















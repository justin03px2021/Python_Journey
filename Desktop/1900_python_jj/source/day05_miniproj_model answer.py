"""
    Mini Project
    Version : 1.0
    Created : 2022.05.26
    Updated : 2022:05.26
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
import time
from colors import *
print("*" * 40)
print(CYAN + "운명의 데스티니 게임 Start" + END)
print("*" * 40)
#1-1. 보물상자를 발견했다는 메시지를 출력하고 사용자가 아무키와 엔터기를 누르기를 기다린다. (보물상자 노란색으로)
#   print, input을 익히기
print('당신은' + YELLOW + ' [보물상자]' + END + '를 획득하였습니다.')
input('아무 키나 누르십시오.')
# 1-2. 보물상자에서 랜덤으로 1개의 무기를 획득한다.
#     각 무기는 [무기이름, 최소공격력, 최대공격력의]의 데이터를 가진다.
#   random, list 익히기
weapon_list = [["휴지",1,3],['목검',3,5],['대검',5,10],['대포',1,50],['에픽밸붕검',50,100]]
import random
rand = random.randint(0,4)
weapon = weapon_list[rand]
print(weapon)

if rand == 0:
    print('당신은 [{}]({}-{})을/를 획득하였습니다.'.format(weapon[0],weapon[1],weapon[2]))
elif rand == 1:
    print('당신은 ' + BLUE + '[{}]({}-{})'.format(weapon[0], weapon[1], weapon[2]) + END + '을/를 획득하였습니다.')
elif rand == 2:
    print('당신은' + RED + '[{}]({}-{})'.format(weapon[0], weapon[1], weapon[2]) + END + '을/를 획득하였습니다.')
elif rand == 3:
    print('당신은' + YELLOW + '[{}]({}-{})'.format(weapon[0], weapon[1], weapon[2]) + END + '을/를 획득하였습니다.')
elif rand == 4:
    print('당신은' + MAGENTA + '[{}]({}-{})'.format(weapon[0], weapon[1], weapon[2]) + END + '을/를 획득하였습니다.')

#2
myimage = 'AAAAAAAAAA'
monimage = ['bbbbbbbbbb','cccccccccc','dddddddddd']

mon_list = [['늑대',1,3],['산적',5,10],['드래곤',1,100]]
rand2 = random.randint(0,2)
mon = mon_list[rand2]
if rand2 == 0:
    print('길을 가다가 당신은 [{}]({}-{})을/를 만났습니다.'.format(mon[0],mon[1],mon[2]))
elif rand2 == 1:
    print('길을 가다가 당신은 ' + BLUE + '[{}]({}-{})'.format(mon[0], mon[1], mon[2]) + END + '을/를 만났습니다.')
elif rand2 == 2:
    print('길을 가다가 당신은 ' + RED + '[{}]({}-{})'.format(mon[0], mon[1], mon[2]) + END + '을/를 만났습니다.')

# 3-1. 초기 양쪽의 에너지는 100이다. my_energy, mon_energy에 저장한다.
my_energy = 100
mon_energy = 100

#3-2 무한루프로 전투를 한다. 무한루프는 둘 중 하나의 에너지가 0 이하가 되면 탈출한다.
while True:
    # 3-3 사용자는 공격 또는 회복을 선택한다.
    while True:
        user_input = input('행동을 선택하세요 (1.공격, 2.회복) : ')
        # if user input == '1' or user_input == '2':
        if user_input in ["1","2"]:
            break
    # 3-4 공격을 선택했다면 최소와 최대 공격력 사이로 공격을 한다.
    if user_input == "1":
        damage = random.randint(weapon[1],weapon[2])
        mon_energy = mon_energy - damage #mon_energy -= damage
        print('당신은 공격으로 {}의 데미지를 입혔습니다. {}의 체력 : {}'.format(damage, mon[0], mon_energy))
        time.sleep(1)

        print(myimage + " " * 11 + monimage[rand2])
        energy_str = ""
        if my_energy > 30:
            energy_str += GREEN_BG + " " * int(my_energy / 5) + END
        else:
            energy_str += RED_BG + " " * int(my_energy / 5) + END

        energy_str += " " * (21 - int(my_energy / 5))

        if mon_energy > 30:
            energy_str += GREEN_BG + " " * int(mon_energy / 5) + END
        else:
            energy_str += RED_BG + " " * int(mon_energy / 5) + END

        print(energy_str)

        if mon_energy <= 0:
            break
    # 3-5 회복은 선택했다면 0 부터 30 까지의 에너지를 회복한다.

    elif user_input == "2":
        heal = random.randint(0,30)
        my_energy = my_energy + heal
        if my_energy > 100:
            my_energy = 100

        # my_energy = (my_energy>100)? 100: my_energy
        print("당신은 회복으로 {}의 에너지가 회복되었습니다. 당신의 에너지 : {}".format(heal, my_energy))
        time.sleep(1)

        print(myimage + " " * 11 + monimage[rand2])
        energy_str = ""
        if my_energy > 30:
            energy_str += GREEN_BG + " " * int(my_energy / 5) + END
        else:
            energy_str += RED_BG + " " * int(my_energy / 5) + END

        energy_str += " " * (21 - int(my_energy / 5))

        if mon_energy > 30:
            energy_str += GREEN_BG + " " * int(mon_energy / 5) + END
        else:
            energy_str += RED_BG + " " * int(mon_energy / 5) + END

        print(energy_str)

    # 3-6 몬스터가 최소와 최대 공격력 사이로 공격을 한다.
    mon_damage = random.randint(mon[1],mon[2])
    my_energy = my_energy - damage
    print('당신은 {}의 공격으로 {}의 피해를 입었습니다. 당신의 에너지 {}'.format(mon[0],mon_damage,my_energy))
    time.sleep(1)
    if my_energy < 0:
        my_energy = 0

    print(myimage + " " * 11 + monimage[rand2])
    energy_str = ""
    if my_energy > 30:
        energy_str += GREEN_BG + " " * int(my_energy / 5) + END
    else:
        energy_str += RED_BG + " " * int(my_energy / 5) + END

    energy_str += " " * (21 - int(my_energy / 5))

    if mon_energy > 30:
        energy_str += GREEN_BG + " " * int(mon_energy / 5) + END
    else:
        energy_str += RED_BG + " " * int(mon_energy / 5) + END

    print(energy_str)

    if my_energy <= 0:
        break
#4. 승리 또는 패배에 따라 메시지를 출력한다.
if my_energy > 0:
    print("{}이/가 말했습니다. 강하군...".format(mon[0]))
    time.sleep(1)
    print("하지만 검은 대륙에는 나보다 강한자가 2917마리나 있다.")
else:
    print("{}이/가 말했습니다. 하하하 상대가 안되는 군 ㅋㅋㅋ...".format(mon[0]))
    time.sleep(1)
    print('내 명품 가방을 가져갔습니다.')
# 5. 프로그램 종료 선언
print("운명의 데스티니 게임 종료 End")


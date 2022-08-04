"""
    1. '이름을 입력하세요 :' 를 출력하고 입력을 받는다.
    2. '최대 숫자를 입력하세요 :' 를 출력하고 입력을 받는다.
    3. 1부터 입력한 수 사이의 임의의 수를 만든다.
    4. 숫자 입력을 받아 임의의 수와 같은지 맞추는 게임을 만든다.
        정답은 몇일까요? 를 출력하고 입력을 받는다.
        임의의 수와 입력한 수가 동일할 때까지 게속한다.
        5번까지 못맞추면 종료한다.
    5. 한 번에 정답을 맞추면 '***님 대단하십니다'
        세 번 이내에 맞추면 '***님 우수한 성적이십니다'
        다섯 번 이내에 맞추면 '***님 좀 심하십니다'
        다섯 번까지 못맞추면 '정답은 * 입니다. *님 사람 맞나요?'
"""
nam = input('이름을 입력하세요 : ')
num = input('최대 숫자를 입력하세요 : ')
while True:
    if num.isdecimal() == True:
        break
    num = input('다시 최대 숫자를 입력하세요 : ')
import random
rand_int = random.randint(1, int(num))
# ans = input('정답을 몇일까요? : ')
# i = 0
# while True and i < 4:
#     if int(ans) == rand_int:
#         if i == 0:
#             print('{}님 대단하십니다.'.format(nam))
#             break
#         elif i <= 2:
#             print('{}님 우수한 성적이십니다.'.format(nam))
#             break
#         else:
#             print('{}님 좀 심하십니다.'.format(nam))
#             break
#     ans = input('정답을 몇일까요? : ')
#     i = i + 1
# if i == 4 and int(ans) == rand_int:
#     print('{}님 좀 심하십니다.'.format(nam))
# if i == 4 and int(ans) != rand_int:
#     print('정답은 {} 입니다. {}님 사람 맞나요?'.format(num,nam))

#4
count = 1
while True:
    ans = input('정답은 몇일까요? ')
    if ans.isdecimal():
        if rand_int == int(ans):
            break
    count = count + 1
    if count > 5:
        break
#5
if count == 1:
    print('{}님 대단하십니다.'.format(nam))
elif count <= 3:
    print('{}님 우수한 성적이십니다.'.format(nam))
elif count <= 5:
    print('{}님 좀 심하시네요.'.format(nam))
else:
    print('정답은 {}입니다. {}님 사람 맞나요?'.format(rand_int, nam))

# correct = False
# for count in range(1,6):
#     ans = input('정답은 몇일까요? ')
#     if ans.isdecimal():
#         if rand_int == int(ans):
#             correct = True
#             break
#
# if count == 1:
#     print('{}님 대단하십니다.'.format(nam))
# elif count <= 3:
#     print('{}님 우수한 성적이십니다.'.format(nam))
# elif count <= 5 and correct == True:
#     print('{}님 좀 심하시네요.'.format(nam))
# else:
#     print('정답은 {}입니다. {}님 사람 맞나요?'.format(rand_int, nam))







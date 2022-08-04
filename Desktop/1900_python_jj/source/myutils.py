import random

def cprintTitle(str):
    col = random.randint(0,255)
    print("\033[38;5;{}m".format(col))
    print("*" * 40)
    print(str)
    print("*" * 40)
    print("\033[0m")

def printExp(str):
    print(str + " => {}".format(eval(str)))

def printMessage1():
    print('***********')

def printMessage2(message):
    print(message)

def printMessage3(message = '입력을 안했음'):
    print(message)

def printMessage4(message='없어', i=5):
    for j in range(i):
        print(message)

def getRandomDice(i=6):
    r = random.randint(1, i)
    return r

def getMultiDice(i=6):
    r1 = random.randint(1,i)
    r2 = random.randint(1, i)
    r3 = random.randint(1, i)
    return r1,r2,r3

def addAll(*i): # *는 1개 이상 될 수 있다는 뜻 / 여러개
    res = 0
    for j in i:
        res += j
    return res

"""
    1. str이 숫자와 '-'로만 구성이 되어있는지 체크
    2. 숫자가 10자리 또는 11자리인지 체크
    3. 10자리이면 XXX, XXX, XXXX return
        11자리이면 XXX,XXXX,XXXX return
    4. 비정상이면 999, 9999, 9999 return
"""
def checkPhoneNumber(str):
    ndigit = 0
    nstring = ""

    #1 숫자와 '-'로만 구성되어 있는지 check
    for c in str:
        if c in "0123456789-":
            if c == '-':
                pass
            else:
                ndigit += 1
                nstring = nstring + c
        else:
            return '999', '9999', '9999'

    #2. 숫자가 10자리인지 11자리인지 check
    if ndigit == 10:
        return nstring[0:3], nstring[3:6], nstring[6:]
    elif ndigit == 11:
        return nstring[0:3], nstring[3:7], nstring[7:]
    else:
        return '999','9999','9999'

def summ(str):
    d = ""
    for c in str:
        d = d + c
    return d



    return '999', '9999', '9999'



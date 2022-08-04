import time

from myutils import *

cprintTitle("Global, Local Variables")

gv = 10

def printvar1():
    print("1단계 gv :", gv)

printvar1()

def printvar2():
    lv = 20
    print("2단계 gv :", gv)
    print("2단계 gv :", lv)
printvar2()

def printvar3():
    lv = 30
    gv = 30
    print("3단계 gv :", gv)
    print("3단계 gv :", lv)
printvar3()

print('3단계 gv : ', gv)

def printvar4():
    lv = 40
    gv = 40
    print("4단계 gv :", gv)
    print("4단계 gv :", lv)

def printvar5():
    lv = 50
    return lv
gv = printvar5()
print('5단계 :', gv)

gv1 = 61
gv2 = 62
def printvar6():
    global gv1
    gv1 = 601
printvar6()

t1 = time.time()
t2 = time.ctime(t1)
t3 = time.strftime('%Y/%m/%d %H:%M:%S')
print(t1)
print(t2)
print(t3)

cprintTitle('file in/out')
s1 = 'we are studying python.'
s2 = '우리는 파이썬을 공부중입니다'
f = open("sample.txt", 'wt', encoding='utf-8')
f.write(s1)
f.write('\n')
f.write(s2)
f.close()

f = open('sample.txt', 'rt')
while True:
    readstr = f.readline()
    if readstr == "":
        break
    print(readstr)

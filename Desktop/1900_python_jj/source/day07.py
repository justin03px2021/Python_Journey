print(eval('2613623+2673283'))

import myutils as mu
mu.cprintTitle("Built-in Functions")
print("1.eval()")
mu.printExp("200 + 500")

print("2.format()")
mu.printExp("format(34567, ',')")
mu.printExp("format(34567, '_')")

mu.printExp("format('꽥꽥꽥꽥꽥', '비<20')")
mu.printExp("format(1234, '0>10')")
mu.printExp("format(1234, '0>+10')")
mu.printExp("format(1234, '<10')")

print("3. str(), float(), int()")
print("str() : " + str(47)+"명이 출석 중")
mu.printExp("float(10)")
mu.printExp("int(10.9)")

print("4.divmod()")
mu.printExp("divmod(10,3)")
a = divmod(10,3)
# a[0] #몫
# a[1] #나머지

b = [1,2,2]; print(b)
c = tuple(b);print(c)
d = set(b);  print(d)

print("5. min(), max()")
c = [1,2,3,4,5]
print(min(c), max(c))
d = ["1000000000000", "2", "A", "a"] #숫자일때는 맨 앞자리만 비교
print(max(d))

print("6. abs(), pow(), sum()")
mu.printExp("abs(-50.5)")
mu.printExp("pow(10,2)")
mu.printExp("sum([100,200,300], 1000)")
g = [[10000,200,300],[10000,500,60000]]
print(max(g))

print("7. round")
mu.printExp("round(234.2)")
mu.printExp("round(234.2, 3)")
mu.printExp("round(2.975, 2)")
mu.printExp("round(2.675, 2)")

print("8. print")
print('010','1234','5678',sep='-',end='|')
print('010',1234,'5678',sep="")

print("9. input")
# input_str = input("아무거나 쳐보세요")
# a,b,c,d = input_str.split(" ")
# print(a,b,c,d)

print("10. len()")
mu.printExp("len('abcde')")
student = ['A1','B2','Z3']
print(len(student))
print(len(student[0]))
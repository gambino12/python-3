'''
    #1st question
week_num = int(input('input week num -> '))
if week_num < 8 and week_num > 0:
    if week_num < 6:
        print('work :(')
    else:
        print('weeknd')
else:
    print('pls input correct num')
    #2nd question

x = int(input('input x -> '))
y = int(input('input y -> '))
z = int(input('input z -> '))
if not(x or y or z) == (not x) and (not y) and (not z):
    print(True)
else:
    print(False)


    #3rd question
x = float(input('input x -> '))
y = float(input('input y -> '))
if x == 0 or y == 0:
    print('uncorrect num')
elif x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')


#4 question
num = int(input('input num -> '))
if num == 1:
    print('x > 0 and y > 0')
elif num == 2:
    print('x < 0 and y > 0')
elif num == 3:
    print('x < 0 and y < 0')
elif num == 4:
    print('x > 0 and y < 0')
elif num > 4 or num < 1:
    print('uncorrect num')

#5 question
import math;
x1 = float(input('input x1 -> '))
y1 = float(input('input y1 -> '))
x2 = float(input('input x2 -> '))
y2 = float(input('input y2 -> '))
a = math.sqrt((x2-x1)**2 +(y2 - y1)**2)
print(round(a,3))
'''


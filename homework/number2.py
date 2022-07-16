'''
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('input number -> '))
sum = 0
lastdigit = num
while num *10%10 != 0:
        num*=10
while num>0:
    lastdigit=num%10
    sum+=lastdigit
    num//=10
print(sum)


#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
n = int(input('input number -> '))
fact = 1
for i in range(n):
    fact += fact * i
print (fact)

#Задана последовательность натуральных чисел, завершающаяся числом 0.
# Требуется определить значение второго по величине элемента в этой последовательности, то есть элемента,который будет наибольшим,
# если из последовательности удалить наибольший элемент.

from random import randint
a = randint(1, 100)
b = randint(1, 100)
c = randint(1, 100)
d = 0
print(a,b,c,d)
for i in range(2):
    if a < b:
        d = a
        a = b
        b = d
    if b < c:
        d = b
        b = c
        c = d

print(b)

#Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
#после чего дробная часть копеек отбрасывается.Требуется определить: через сколько лет вклад составит не менее Y рублей.

x, p, y = int(input('input x -> ')),int(input('input p -> ')),int(input('input y -> '))
year = 0
while x < y:
    year += 1
    x +=  x / 100 * p
    print (x)
print( year , '- лет понадобится ')
'''

'''
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def sumeoflemnts(Arr):
    sum = 0
    for i in range(1,len(Arr),2):
        if i == 0:
            i += i
        else:
            sum = sum + Arr[i]         
    return sum
    




list_1 = [2,6,8,9,5,3,9,1]
print(sumeoflemnts(list_1))

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def pairsnum(arr):

    for i in range(len(arr)):
        if i == len(arr) // 2 and len(arr) %2 == 0:
            return 
        if i > len(arr) // 2 and len(arr) %2 != 0:
            return
        resalt = []
        resalt =  arr[i] * arr[(i+1)*(-1)]
        print(resalt)
    
list_2 = [5, 7, 2, 1, 4, 1]
print(pairsnum(list_2))

#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов
def qwe(arr): ##эту задачку не смог осилить,сегодня просто дедлайн ,а я хочу еще посмотреть лекцию и семинар :(
    min = arr[0]
    max = arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] % 1 < min:
            min = arr[i+1] % 1
        else:
            max = arr[i+1] % 1
    result = max - min
    print(min,max)

list_3 = [5.2,3.8,3.5]

print(qwe(list_3))
'''
#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def sek(num):
    num2 = ''   
    while num > 0:
        num2 = str(num % 2) + num2
        num = num // 2
    print(num2)
##ps подсмотрел в инете,  сначало вспоминал в к сшарпе делал потом плюс минус к этому решению пришел но подсмотрел в инете что можно не парится и сделать строку  

n = int(input('input num -> '))
print(sek(n))


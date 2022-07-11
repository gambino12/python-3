'''
# 1st question

a = int(input('input a -> '))
b = int(input('input b -> '))
if a * a == b or b * b == a:
    print('yes')
else:
    print('no')
##
# 2nd question

N = int(input('input N -> '))
N = N * (-1)
print(*range(N,N*(-1)+1))


#3rd question
a = float(input('input a -> '))
a = a * 10 % 10
print(int(a))

#4 question
N = int(input('input N -> '))
if N % 5 == 0 or N % 10 == 0 or N % 15 == 0 and N % 30 != 0:
    print('yes')
else:
    print('no')
  '''  




# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

## модуль числа abs()
## может быть решение короче через разницу

from random import randint
n = int(input('Введите количество элементов в массиве: '))
a = []
for i in range(n):
    a.append(randint(1, 10))
print(*a)
x = k2 = 3
k1 = x - 1
print(x)
flag = True
while flag:
    k1 += 1
    i = 0
    while i < n and flag:
        if a[i] == k1:
            print(f'=> {i}')
            flag = False
        else: 
            i += 1
    k2 -= 1
    i = 0
    while i < n and flag:
        if a[i] == k2:
            print(f'=> {i}')
            flag = False
        else: 
            i += 1
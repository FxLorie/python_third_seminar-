# Задача №23. Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list = [0, -1, 5, 2, 3]
list_1 = []
for i in range(len(list)-1):
    if list[i] < list[i+1]:
        list_1.append(f'{list[i]} < {list[i+1]}')
print(f'{len(list_1)} {list_1}')

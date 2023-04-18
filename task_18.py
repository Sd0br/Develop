#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
lst = []
N = int(input("Введите количестко элементов массива: "))
for i in range(N):
    lst.append(random.randint(1,100))
print(lst)
number = int(input("Введите число: "))
raznica = abs(number - lst[0])
minimum = 0
for i in lst:
    if abs(number - i) <= raznica:
        raznica = abs(number - i)
        minimum = i
print(minimum)




#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
lst = []
N = int(input("Введите количестко элементов массива: "))
for i in range(N):
    lst.append(random.randint(1,100))
print(lst)
number = int(input("Введите число: "))
count = 0
for y in lst:
    if y == number:
        count += 1
print(f"Число {number} встречается {count} раз")


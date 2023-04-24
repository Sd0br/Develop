# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def summa(num_1, num_2):
    if num_2 == 1:
        return num_1 + 1
    else:
        return 1 + summa(num_1, num_2 - 1)


a = int(input())
b = int(input())
print(summa(a, b))
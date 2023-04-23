# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

#возводит число num_1 в степень num_2
def stepen(num_1, num_2):
    if num_2 == 2:
        return num_1 * num_1
    else:
        return num_1 * stepen(num_1, num_2 - 1)
    
a = int(input())
b = int(input())
print(stepen(a, b))
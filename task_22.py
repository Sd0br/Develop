#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
set_1 = set()
set_2 = set()
for i in range(n):
    set_1.add(int(input("Введите число: ")))
for i in range(m):
    set_2.add(int(input("Введите число: ")))
print(set_1)
print(set_2)
set_3 = set_1.union(set_2)
print(set_3)




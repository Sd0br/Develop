#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
#Выведите минимальное количество монет, которые нужно перевернуть



kolichestvo_monet = int(input("Введите количество монет: "))
monety = input(f"Введите последовательность из {kolichestvo_monet} 0 и 1 ")
kolichestvo0 = 0
kolichestvo1 = 0
i = 0
while i < kolichestvo_monet:
    if monety[i] == "0":
        kolichestvo0 +=1
    if monety[i] == "1":
        kolichestvo1 +=1
    i += 1
#print(kolichestvo0)
#print(kolichestvo1)
if kolichestvo0 == kolichestvo_monet or kolichestvo1 == kolichestvo_monet:
    print("Ничего переворачивать ненужно")
elif kolichestvo0 < kolichestvo1:
    print(f"Нужно перевернуть {kolichestvo0} монет")
else:
    print(f"Нужно перевернуть {kolichestvo1} монет")

    
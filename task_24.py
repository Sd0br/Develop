from random import randint
gryadki = int(input("Введите количество грядок: "))
yagody = [randint(1, 100) for i in range(gryadki)]
print(yagody)
maksimum = 0
for y in range(1, len(yagody) - 1):
    if maksimum < yagody[y-1] + yagody[y] + yagody[y+1]:
        maksimum = yagody[y-1] + yagody[y] + yagody[y+1]
print(maksimum)


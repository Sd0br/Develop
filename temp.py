maxim = 0
count = 0
amount_days = int(input("Введите количество дней "))
for i in range(amount_days):
    temp = int(input(f"Введите температуру в {i+1} день "))
    if temp > 0:
        count += 1
        if count > maxim:
            maxim = count
    else:
        count = 0

print(f"Максимальная оттепель длилась {maxim} дней")-4



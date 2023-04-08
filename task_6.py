numberStr = input("Введите номер билета 6 цифр: ")
firstSum = 0
secondSum = 0
for i in range(3):
    firstSum = firstSum + int(numberStr[i])
print(firstSum)
for i in range(3,6):
    secondSum = secondSum + int(numberStr[i])
print(secondSum)
if firstSum == secondSum:
    print("Билет счастливый")
else:
    print("Билет несчастливый")

     

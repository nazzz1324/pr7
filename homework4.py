a = int(input("Введите  число a: "))
b = int(input("Введите  число b (b не должно быть равно 0): "))
c = int(input("Введите число c: "))

if b != 0:
    result = a / b - 2 * c
    print(f"Результат в десятичной системе: {result}")

else:
    print("Ошибка: b не должно быть равно 0.")


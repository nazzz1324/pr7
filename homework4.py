def convert(n):
    if n < 4:
        return str(n)
    else:
        return convert(n // 4) + str(n % 4)


a = input("Введите целое простое число a: ")
b = input("Введите целое простое число b (b не должно быть равно 0): ")
c = input("Введите целое простое число c: ")

if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)

    if b != 0:
        result = a / b - 2 * c
        print(f"Результат в десятичной системе: {result}")
        print(f"Результат в четверичной системе: {convert(int(result))}")
    else:
        print("Ошибка: b не должно быть равно 0.")
else:
    print("Ошибка: введите корректные целые числа.")

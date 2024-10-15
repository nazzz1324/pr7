def convert(n):
    if n < 4:
        return str(n)
    else:
        return convert(n // 4) + str(n % 4)

number = input("Введите целое простое десятичное число: ")

if number.isdigit():
    number = int(number)
    print(f"Четверичное представление: {convert(number)}")
else:
    print("Ошибка: введите корректное целое число.")

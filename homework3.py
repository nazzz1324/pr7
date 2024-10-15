def convert(n):
    if n < 4:
        return str(n)
    else:
        return convert(n // 4) + str(n % 4)

number = input("Введите целое десятичное число: ")

if number.lstrip('-').isdigit():
    number = int(number)
    if number < 0:
        print(f"Четверичное представление: {'-' + convert(abs(number))}")
    else:
        print(f"Четверичное представление: {convert(number)}")
else:
    print("Ошибка: введите корректное целое число.")

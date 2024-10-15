number = input("Введите целое десятичное число: ")

if number.lstrip('-').isdigit():
    number = int(number)
    if number >= 0:
        bin = bin(number)[2:]
        oct = oct(number)[2:]
    else:
        bin = '-' + bin(abs(number))[2:]
        oct = '-' + oct(abs(number))[2:]
    print(f"Двоичное представление: {bin}")
    print(f"Восьмеричное представление: {oct}")
else:
    print("Ошибка: введите корректное целое число.")

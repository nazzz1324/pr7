number = input("Введите целое простое десятичное число: ")

if number.isdigit():
    number = int(number)
    print(f"Двоичное представление: {bin(number)[2:]}")
    print(f"Восьмеричное представление: {oct(number)[2:]}")
else:
    print("Ошибка: введите корректное целое число.")

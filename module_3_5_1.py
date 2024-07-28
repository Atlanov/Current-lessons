print("Рекурсивное умножение цифр")
number = int(input('Введите Ваши цифры в виде целого числа: '))


if number % 10 != 0:
    def get_multiplied_digits(number):

        str_number = str(number)
        if len(str_number) <= 1:
            return number
        else:
            first = str_number[0]
        return int(first) * get_multiplied_digits(int(str_number[1:]))


    result = get_multiplied_digits(number)
    print(f"Ваш результат (при этом '0' учтён как отсутствие цифры): {result}")
else:
    def get_multiplied_digits(number):
        str_number = str(number)

        if len(str_number) <= 1:
            return number
        else:
            str_number = str_number[::-1]
            str_number = int(str_number)
            str_number = str(str_number)
            first = str_number[0]
        return int(first) * get_multiplied_digits(int(str_number[1:]))


    result = get_multiplied_digits(number)
    print(f"Ваш результат (при этом '0' учтён как отсутствие цифры): {result}")

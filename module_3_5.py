print("Рекурсивное умножение цифр")
number = int(input('Введите Ваши цифры в виде целого числа, не кратного 10: '))
#На досуге постараюсь разобраться с числами, кратными 10, но это не входит в задание

def get_multiplied_digits(number):

    str_number = str(number)
    if len(str_number) <= 1:
        return number
    else:
        first = str_number[0]
    return int(first) * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(number)
print(f"Ваш результат (при этом '0' учтён как отсутствие цифры): {result}")

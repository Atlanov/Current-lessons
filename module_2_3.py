print('Стиль кода часть II. Цикл While')
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a >= 0 or a < len(my_list):
    if my_list[a] > 0:
        print(my_list[a])
        a = a + 1
    elif my_list[a] == 0:
        a = a + 1
        continue
    else:
        break

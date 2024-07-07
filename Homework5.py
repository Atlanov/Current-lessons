mutable_list = [1,2,3,'one','two','three',True]#Начинаем с 4-го пункта задания, предположив, что на 3-м программа остановится
print("Объект:",mutable_list)
mutable_list[3:] = 'six','one','three','ten',False
print("Новый объект:",mutable_list)
immutable_var = 7,8,9,'nine','eight','seven'
print("Другой объект:",immutable_var)
print("Элемент 1:",immutable_var[0])
immutable_var[0] = 6
print("Изменённый объект:",immutable_var)#Такой объект (кортеж) изменить невозможно
print("Распаковка позиционных параметров")


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(10, 'number', False)
print_params(15)
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [5, 'cross', True]
values_dict = {'a': 33, 'b': 'cows', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

print('Работа "Пространство имён" с использованием функций')
calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    x = len(string),string.upper(),string.lower()
    count_calls()
    return x


def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    for i in range(0, len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    if string in list_to_search:
        x = True
    else:
        x = False
    return x


print(string_info('Revolution'))
print(string_info('Execution'))
print(string_info('Congratulation'))
print(is_contains('VIdi',['Veni','vidi','vici']))
print(is_contains('ratio',['Citius', 'altius', 'fortius']))
print(f"Всего функции использовались {calls} раз")

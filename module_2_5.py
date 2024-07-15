print('The function (with a parameter): "get_matrix(n, m, value)"')


def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        element = []
        for j in range(0, m):
            element.append(value)
        matrix.extend([element])
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print('Constructed matrices:')
print(result1)
print(result2)
print(result3)  # Пустые строки добавились при исправлении жёлтых подчёркиваний

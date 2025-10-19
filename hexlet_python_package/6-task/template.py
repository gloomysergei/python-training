# Изменяет первый список напрямую
# В данном случае такая реализация оправдана
def append(data1, data2):
    for item in data2:
        data1.append(item)

def flatten(matrix):
    result = []
    for item in matrix:
        length_transposed = len(item)
        append(result, item)  # распрямили список
    i = 0
    step = length_transposed
    transposed = []
    while i < length_transposed:
        inner = result[i::step]
        transposed.append(inner)
        i += 1
    return transposed

matrix = [[1]]
# result = flatten(matrix)
# print(result) # [1, 2, 3, 4, 5, 6]
# lst = []
# inner = result[0::2] # STEP - длина внутреннего спсика матрицы
# lst.append(inner)
# inner = result[1::2]
# lst.append(inner)
print(flatten(matrix))


       

def append(data1, data2):
    for item in data2:
        data1.append(item)

def transposed(matrix):
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
result = transposed([[1, 2], [3, 4], [5, 6]]) # [[1, 3, 5], [2, 4, 6]]
print(result)

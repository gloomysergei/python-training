# BEGIN
def transposed(matrix):
    result = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        result.append(new_row)
    return result


""" Альтернативное решение с использованием zip и оператора распаковки
def transposed(matrix):
    result = []
    for column in zip(*matrix):
        result.append(list(column))
    return result
"""
# END
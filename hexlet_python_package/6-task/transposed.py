def transposed(matrix):
    transposed_matrix = []
    row_transposed_one = []
    row_transposed_two = []
    for row_matrix in matrix:
        length = len(row_matrix)
        [one, two] = row_matrix
        row_transposed_one.append(one)
        row_transposed_two.append(two)
    transposed_matrix.append(row_transposed_one)
    transposed_matrix.append(row_transposed_two)
    return transposed_matrix

result = transposed([[1, 2], [3, 4], [5, 6]]) # [[1, 3, 5], [2, 4, 6]]
print(result)
# каждый внутренний список  - это строка матрицы
# надо взять надо взять элемент каждого списка и получим строку transposed_matrix
# 1. создать результирующий список - transposed_matrix = []
# 2. создать внутренний список для новых строк - row_transposed = []
# 3. пройти for in matrix:
#    - число строк transposed_matrix = len(row_matrix) = 2
#    - значит вне for надо создать: 
#       * row_transposed_one
#       * row_transposed_two
# 4. получаем первый row_matrix - 
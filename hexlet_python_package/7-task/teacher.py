# Определяем функцию для вычисления факториала
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def triangle(row_number):
    numbers_count = row_number + 1
    line = []
    calculated = fact(row_number)
    for i in range(numbers_count):
        # Для вычисления числа заданной строки используем формулу
        # расчёта биноминальных коэффициентов С(n, k) = n! / (k! * (n - k)!)
        line.append(calculated / (fact(i) * fact(row_number - i)))
    return line


# Alternative solutions
#
#
# def triangle(row):
#     line = [1]
#     for i in range(row):
#         line.append(line[i] * ((row - i) / (i + 1)))
#     return line
#
#
# from operator import add
#
#
# def triangle(row_number):
#     row = [1]
#     for _ in range(row_number):
#         row = list(map(  # [x,y,z]
#             add,         # x y z 0
#             row + [0],   # + + + +
#             [0] + row,   # 0 x y z
#         ))
#     return row
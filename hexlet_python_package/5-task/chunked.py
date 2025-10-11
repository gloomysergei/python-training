def chunked(number, sequence):
    result = []
    start = 0
    end = number
    while (end - number) < len(sequence):
        inner_sequence = sequence[start:end]
        result.append(inner_sequence)
        start += number
        end += number
    return result

result = chunked(2, 'abcdf')  # [['a', 'b'], ['c', 'd']]
print(result)
# Для алгоритма нужно нечто общее, объединяющее list, tuple, string.
# вероятно - это срезы
# Какой пограничный случай - когда будет останов

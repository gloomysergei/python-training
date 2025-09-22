# какой алгоритм придумать - 
# фиксируем первое число в последовательности
# формируем следующее число +1
# сравниваем его с вторым числом последовательности
# если не == то False? если === продолжаем проверку
def is_continuous_sequence(coll):
    if len(coll) == 0 or len(coll) == 1:
        return False
    first = coll[0]
    for item in coll:
        if first == item:
            first += 1
        else:
            return False
    return True

result = is_continuous_sequence([7]) # False
print(result)
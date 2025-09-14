
def translate_even_number(number):
    result = []
    temp = number
    while temp >= 1:
        if temp % 2 == 0:
            result.append(1)
            temp = temp // 2
        elif temp % 2 == 1:
            result.append(0)
            temp = (temp - 1) // 2
    return result

def translate_odd_number(number):
    result = []
    temp = number
    while temp >= 1:
        if temp % 2 == 1:
            result.append(1)
            temp = (temp - 1) // 2
        elif temp % 2 == 0:
            result.append(0)
            temp = temp // 2
    return result

def hamming_weight(number):
    count = 0
    if number % 2 == 0:
        result = translate_even_number(number)
    else:
        result = translate_odd_number(number)
    for item in result:
        if item == 1:
            count += 1
    return count